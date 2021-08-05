from argparse import Namespace
from pathlib import Path
from typing import NamedTuple

from jax.numpy import ndarray


class FLAGS(Namespace):
    duration_lstm_dim = 256
    vocab_size = 256
    duration_embed_dropout_rate = 0.5
    num_training_steps = 200_000
    postnet_dim = 512
    prenet_dim = 256
    acoustic_decoder_dim = 512
    acoustic_encoder_dim = 256

    # dataset
    max_phoneme_seq_len = 128 * 3
    max_wave_len = 1024 * 64 * 3
    data_mean = -5.3  # infore mel-spectrogram mean
    data_std = 1.8  # infore mel-spectrogram std

    # Montreal Forced Aligner
    special_phonemes = ["sil", "sp", "spn", " "]  # [sil], [sp] [spn] [word end]
    sil_index = special_phonemes.index("sil")
    sp_index = special_phonemes.index("sp")
    word_end_index = special_phonemes.index(" ")

    # dsp
    mel_dim = 80
    sample_rate = 16000
    n_fft = 1024
    window_length = 1024
    hop_length = 256
    fmin = 0.0
    fmax = 8000

    # training
    batch_size = 16
    learning_rate = 1.25e-4
    duration_learning_rate = 1e-4
    max_grad_norm = 1.0
    weight_decay = 1e-4
    steps_per_update = 10

    # ckpt
    ckpt_dir = Path("ckpts")
    data_dir = Path("train_data")


class DurationInput(NamedTuple):
    phonemes: ndarray
    lengths: ndarray
    durations: ndarray


class AcousticInput(NamedTuple):
    phonemes: ndarray
    lengths: ndarray
    durations: ndarray
    wavs: ndarray
    wav_lengths: ndarray
    mels: ndarray
