import math, wave, array, sys

def bandIndex(toneInput):
	tones = [['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]

	up = -1
	low = -1

	for i in range(0,4):
		for j in range(0,4):
			if str(tones[i][j]) == str(toneInput):
				up = j
				low = i
				return up, low
	
	print ("\nERROR: Input is not valid\n")
	sys.exit()	


print ("\n 1 2 3 A \n" 
" 4 5 6 B \n" 
" 7 8 9 C \n"
" * 0 # D \n")

toneInput = input("> Select tone: ")

up, low = bandIndex(toneInput)

lower = [697, 770, 852, 941]
upper = [1209, 1336, 1477, 1633]

print ("\nUpper Band:", upper[up])
print ("Lower Band:", lower[low])

duration = 1 # seconds
volume = 20 # percent
data = array.array('h') # signed short integer (-32768 to 32767) data
sampleRate = 44100 # of samples per second (standard)
numChan = 1 # of channels (1: mono, 2: stereo)
dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
numSamples = sampleRate * duration

freqLower = lower[low] # of cycles per second (Hz) (frequency of the sine waves)
freqUpper = upper[up] # of cycles per second (Hz) (frequency of the sine waves)

numSamplesPerCycLower = int(sampleRate / freqLower)
numSamplesPerCycUpper = int(sampleRate / freqUpper)


for i in range(numSamples):
    sample = 32767 * float(volume) / 100
    sinLower = math.sin(math.pi * 2 * (i % numSamplesPerCycLower) / numSamplesPerCycLower)
    sinUpper = math.sin(math.pi * 2 * (i % numSamplesPerCycUpper) / numSamplesPerCycUpper)
    sample *= (sinLower + sinUpper)
    data.append(int(sample))

if str(toneInput) == '*':
	toneInput = 'x'

f = wave.open('Tone_' + str(toneInput) + '.wav', 'w')
f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
f.writeframes(data.tostring())
f.close()

print ("\nTone_" + str(toneInput) + ".wav created!\n")