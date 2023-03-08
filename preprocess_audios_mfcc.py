import multiprocessing
from functools import partial
from tqdm import tqdm
import librosa

def preprocess_audio_mfcc(audio_file,sr,duration,n_mfcc):
    # Load audio file
    audio, sr = librosa.load(audio_file, sr=sr,mono=True,offset=0.0, duration=duration)
    
    # Convert audio to MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    
    # Pad or truncate MFCC to a fixed length
    # max_length = 1000
    # if mfcc.shape[1] < max_length:
    #    mfcc = np.pad(mfcc, pad_width=((0, 0), (0, max_length - mfcc.shape[1])), mode='constant')
    # else:
    #    mfcc = mfcc[:, :max_length]

    return mfcc

def preprocess_audios_mfcc(audio_files,num_processes,sr=22050,duration=5.0,n_mfcc=40):
    pool = multiprocessing.Pool(num_processes,sr=sr,duration=duration,n_mfcc=n_mfcc)
    func = partial(preprocess_audio_mfcc)
    
    mfccs = []
    with tqdm(total=len(audio_files)) as pbar:
        for mfcc in pool.imap(func, audio_files):
            mfccs.append(mfcc)
            pbar.update(1)
            
    pool.close()
    pool.join()
    return mfccs