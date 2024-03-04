импортировать torch 
импортировать numpy как Numpy 
импортировать nemo.collections.asr как nemo_asr

def_greedy(файлы, asr_model):
 расшифровки = asr_model.transcribe(файлы, размер пакета = 20)
 возвращает расшифровки

if __name__ == '__main__': 
 модель = "QuartzNet15x5_golos.nemo"
 asr_model = nemo_asr.models.EncDecCTCModel.restore_from(модель)
 файлы = ["examples_data_001ce26c07c20eaa0d666b824c6c6924.wav"]
 условные обозначения = infer_greedy(файлы, asr_model)
 печать (условные обозначения)