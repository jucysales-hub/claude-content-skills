"""Transcreve um reel: tenta o áudio (faster-whisper) e, se o modelo não baixar, lê as legendas
queimadas na tela por OCR (rapidocr). Também gera grades de frames para análise visual.

Uso: python3 transcrever.py video.mp4 [saida_dir]
Dependências: ffmpeg; pip install faster-whisper rapidocr_onnxruntime
"""
import glob
import os
import subprocess
import sys


def sh(*args):
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def transcrever_audio(video, out):
    from faster_whisper import WhisperModel

    wav = os.path.join(out, "audio.wav")
    sh("ffmpeg", "-y", "-i", video, "-ac", "1", "-ar", "16000", wav)
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(wav, language="pt")
    return [f"[{s.start:5.1f}s] {s.text.strip()}" for s in segs]


def ocr_legendas(video, out, fps=4):
    from rapidocr_onnxruntime import RapidOCR

    fdir = os.path.join(out, "ocr_frames")
    os.makedirs(fdir, exist_ok=True)
    sh("ffmpeg", "-y", "-i", video, "-vf", f"fps={fps},scale=540:-1", "-q:v", "3", f"{fdir}/%04d.jpg")
    eng = RapidOCR()
    linhas, prev = [], None
    for p in sorted(glob.glob(f"{fdir}/*.jpg")):
        t = (int(os.path.basename(p)[:4]) - 1) / fps
        r, _ = eng(p)
        txt = " | ".join(x[1] for x in (r or []) if float(x[2]) > 0.6)
        if txt and txt != prev:
            linhas.append(f"[{t:5.1f}s] {txt}")
        prev = txt
    return linhas


def main():
    video = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(video)[0] + "_analise"
    os.makedirs(out, exist_ok=True)
    sh("ffmpeg", "-y", "-i", video, "-vf", "fps=1/4,scale=360:-1,tile=4x3", f"{out}/grade_%02d.jpg")
    try:
        linhas, fonte = transcrever_audio(video, out), "audio"
    except Exception as e:
        print(f"Transcrição de áudio indisponível ({type(e).__name__}); usando OCR das legendas.")
        linhas, fonte = ocr_legendas(video, out), "ocr"
    path = os.path.join(out, f"transcricao_{fonte}.txt")
    with open(path, "w") as f:
        f.write("\n".join(linhas) + "\n")
    print(f"Transcrição ({fonte}): {path}\nGrades de frames: {out}/grade_*.jpg")


if __name__ == "__main__":
    main()
