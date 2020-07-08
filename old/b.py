from apiclient.discovery import build
import json

YOUTUBE_API_KEY = 'AIzaSyAJSqfn6R-4aejowYRDdLtaQ5t7B4ShyC0'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    #検索したい文字列を指定
    q='プログラミング',
    #視聴回数が多い順に取得
    order='viewCount',
    type='video',
).execute()

# for key, val in search_response.items():
    # print(key, val)

print('検索ワード :', 'プログラミング')
print('--------')
for cnt in range(4):
    print('再生回数 :', cnt+1, '位')
    print('チャンネル名 :', search_response['items'][0]['snippet']['channelTitle'])
    print('動画タイトル :', search_response['items'][cnt]['snippet']['title'])
    print('--------')


    
