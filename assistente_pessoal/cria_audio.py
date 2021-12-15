from gtts import gTTS
from playsound import playsound

def cria_audio_e_toca(audio, nome):
    tts = gTTS(audio, lang="pt-br")
    tts.save('aula/assistente_pessoal/audios/{}.mp3'.format (nome))
    print ("Nami: ", audio)
    playsound('aula/assistente_pessoal/audios/{}.mp3'.format (nome))



cria_audio_e_toca("Espera aí", "Feedback")

playsound('aula/assistente_pessoal/audios/link_start.mp3')
playsound('aula/assistente_pessoal/audios/nya_button.mp3')
playsound('aula/assistente_pessoal/audios/megumu_yamerooo.mp3')
playsound('aula/assistente_pessoal/audios/Ayaya.mp3')



