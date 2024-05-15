#Setting up API and upload the file from user to database
def array_to_string(string1):
    finalstr = ""
    for i in string1:
        finalstr = finalstr + "\n" + "*" + i
    return finalstr

def sound_to_name (filepath):
    from acrcloud.recognizer import ACRCloudRecognizer

    if __name__ == '__main__':
        config = {
        #Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
        'host':'identify-ap-southeast-1.acrcloud.com',
        'access_key':'25aa55f23c66a1261c1e5b15859139e6',
        'access_secret':'qEWj8qvi54zGYVpe7sOEcOYIeYicceUXOUEEvCRH',
        'timeout':10 # seconds
        }

        '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, api de, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
        re = ACRCloudRecognizer(config)

        #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
        ans = re.recognize_by_file(filepath, 0)
        return ans

#Remove duplicate item to eliminate the same ans
def remove_duplicate_item(array):
    finalarray = []
    for i in array:
        if i not in finalarray:
            finalarray.append(i)

    return finalarray

#Filter out the JSON file to a simple string for communication between backend and frontend
def filter_out_name(string1):
    ans = ""
    ansarr_song = []
    ansarr_artist  = []
    ansarr_yt = []

    #find song name and artist
    for i in range(len(string1)-3):
        #find track name
        if (string1[i]=="t" and string1[i+1] == "r" and string1[i+2] == "a" and string1[i+3] == "c" and string1[i+4] == "k"):
            if (string1[i+9] == "i" and string1[i+10] == "d"): #check if there is id or not
                index_of_first_name = string1.index("name", i+14)
                for j in range(index_of_first_name+7,len(string1)):
                    ans = ans + string1[j]
                    if (string1[j+1]== '"'):
                        break
                ansarr_song.append(ans)
                ans = ""
            else:
                for j in range(i+16,len(string1)):
                    ans = ans + string1[j]
                    if (string1[j+1]== '"'):
                        break
                ansarr_song.append(ans)
                ans = ""

        #find artists created the song
        if (string1[i]=="a" and string1[i+1] == "r" and string1[i+2] == "t" and string1[i+3] == "i" and string1[i+4] == "s" and string1[i+5] == "t"):
            if (string1[i+12] == "i" and string1[i+13] == "d"): #check if there is id or not
                index_of_first_name = string1.index("name", i+14)
                for j in range(index_of_first_name+7,len(string1)):
                    ans = ans + string1[j]
                    if (string1[j+1]== '"'):
                        break
                ansarr_artist.append(ans)
                ans = ""

            else:
                for j in range(i+19,len(string1)):
                    ans = ans + string1[j]
                    if (string1[j+1]== '"'):
                        break
                ansarr_artist.append(ans)
                ans = ""

    #find youtube link
    for i in range(len(string1)-2):
        if(string1[i] == "y" and string1[i+3] == "t" and string1[i+4] == "u" and string1[i+5] == "b" and string1[i+6] == "e"):
            for j in range(i+17, len(string1)):
                ans = ans + string1[j]
                if (string1[j + 1] == '"'):
                    break
            ansarr_yt.append(ans)
            ans = ""

    finalarr_song = remove_duplicate_item(ansarr_song)
    finalarr_artist = remove_duplicate_item(ansarr_artist)
    finalarr_yt = remove_duplicate_item(ansarr_yt)


    #Output song for user
    song_headline = "-The song matched the most:"
    strans = array_to_string(finalarr_song)


    #Output artist for user
    artist_headline = "-The artist matched the most:"
    strans1 = array_to_string(finalarr_artist)



    #Output link for users
    strans2 = "-The Youtube link matched the most:"
    if (len(finalarr_yt) == 0):
        strans2 = strans2 + "\n" + "*" + "None"
    else:
        for i in finalarr_yt:
            strans2 = strans2 + "\n" + "*" + "https://www.youtube.com/watch?v=" + i


    #Connect all string
    totalstrans = song_headline + strans + "\n" + artist_headline + strans1 + "\n" + strans2


    return totalstrans


#Read and write the ans and the path name
open_txt = open("/Users/admin/Documents/pathname1.txt", "r")
f = open("/Users/admin/Documents/ansresult.txt","w")
s = filter_out_name(sound_to_name(open_txt.read()))
print(s)
#b = s.rstrip(", ")
#f.write(b)