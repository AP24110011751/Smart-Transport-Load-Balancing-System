size=int(input("enter no of songs:"))
songs=[]
for i in range(size):
    songs.append(int(input(f"enter {i+1} song duration:")))
total_duration=sum(songs)
total_songs=len(songs)
invalid = False
for duration in songs:
    if duration <= 0:
        invalid = True
        break

if invalid:
    print("\nInvalid Duration")
else:
    print("\nTotal Duration:", total_duration, "seconds")
    print("Songs:", total_songs)

    if total_duration < 300:
        print("Category: Too Short Playlist")
        print("Recommendation: Add more songs")

    elif total_duration > 3600:
        print("Category: Too Long Playlist")
        print("Recommendation: Reduce playlist length")
    count=0
    for i in range(size):
      for j in range(i + 1, size):
        if songs[i] == songs[j]:
                count += 1

    if count > 0:
        print("Category: Repetitive Playlist")
        print("Recommendation: Add variety")


    elif (max(songs) - min(songs)) <= 300:
        print("Category: Balanced Playlist")
        print("Recommendation: Good listening session")

    else:
        print("Category: Irregular Playlist")
        print("Recommendation: Adjust playlist for better balance")