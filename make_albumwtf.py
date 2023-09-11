#make_album


def make_album(artist_name,title,number_of_songs):
    records = {}
    for records in range(3):
        key=band_name
        value=record_name
        records[key]=value
    return records
        
    

while True:
   band_name = input("\nEnter name of band/artist: ")
   print("enter 'q' at anytime to quit.")
   if band_name == 'q':
    break
        

   record_name = input("\nEnter the name of one of their albums: ")
   print("enter 'q' at anytime to quit.")
   if record_name == 'q':
    break

   songs = input('\nhow many songs are on that album?: ')
   if songs == 'q':
    break
   
   


rocknroll = make_album(any,any,any)
print(rocknroll)
