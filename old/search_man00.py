from apiclient.discovery import build
import json


YOUTUBE_API_KEY = 'AIzaSyAJSqfn6R-4aejowYRDdLtaQ5t7B4ShyC0'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


# キーワードで動画視聴回数順に検索する関数
def get_video_ranking(my_part, my_q, my_order, my_type, my_num):
    # search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults='50', videoDuration='short', pageToken='CDIQAA').execute()
    search_response = youtube.search().list(part=my_part, q=my_q, order=my_order, type=my_type, maxResults=my_num).execute()

    # ランキング順に動画のIDを格納する変数
    video_id_ranking_list = []

    print('検索ワード :', my_q)
    print('検索数 :', my_num)
    print('--------')
    for cnt in range(my_num):
        # print('再生回数 :', cnt+1, '位')
        # print('チャンネル名 :', search_response['items'][cnt]['snippet']['channelTitle'])
        # print('動画タイトル :', search_response['items'][cnt]['snippet']['title'])
        # print('動画サムネイルURL :', search_response['items'][cnt]['snippet']['thumbnails']['default']['url'])
        # print('動画投稿日 :', search_response['items'][cnt]['snippet']['publishTime'])
        # print('VideoID :', search_response['items'][cnt]['id']['videoId'])
        # print('ChannelID :', search_response['items'][cnt]['snippet']['channelId'])
        # print('NextPageToken :', search_response['nextPageToken'])
        # print('--------')

        # ランキング順に動画のIDを格納
        video_id_ranking_list.append(search_response['items'][cnt]['id']['videoId'])

    return search_response, video_id_ranking_list


# 動画IDから動画の詳細を取得する関数
def get_video_detail(video_id_ranking_list):

    ranking_number = 0

    for video_id in video_id_ranking_list:
        ranking_number += 1

        print('---')
        # 動画1件あたりの詳細を代入
        video_data = youtube.videos().list(part='statistics, snippet, contentDetails', id=video_id).execute()

        # # その他情報
        # print('動画の再生回数順位 :', ranking_number)
        # print('動画のID :', video_id)

        # # 動画1件あたりの欲しい情報を抽出
        # print('動画のタイトル :', video_data['items'][0]['snippet']['title'])
        # # print('動画の説明 :', video_data['items'][0]['snippet']['description'])
        # print('動画の視聴回数 :', video_data['items'][0]['statistics']['viewCount'])
        # print('動画のアップデート日時 :', video_data['items'][0]['snippet']['publishedAt'])
        # print('動画のサムネイル画像URL :', video_data['items'][0]['snippet']['thumbnails']['default']['url'])
        # print('動画の長さ :', video_data['items'][0]['contentDetails']['duration'])
        # try :
        #     print('動画のキーワドタグ :', video_data['items'][0]['snippet']['tags'])
        # except Exception as e:
        #     print('動画のキーワドタグ :', 'この動画にキーワードタグはありません')
        # print('動画のカテゴリID :', video_data['items'][0]['snippet']['categoryId'])
        # try:
        #     print('動画の高評価数 :', video_data['items'][0]['statistics']['likeCount'])
        # except Exception as e:
        #     print('動画の高評価数 :', 'この動画に動画の高評価数はありません')
        # try:
        #     print('動画の低評価数 :', video_data['items'][0]['statistics']['dislikeCount'])
        # except Exception as e:
        #     print('動画の低評価数 :', 'この動画に動画の低評価数はありません')
        # try:
        #     print('動画のコメント数 :', video_data['items'][0]['statistics']['commentCount'])
        # except Exception as e:
        #     print('動画のコメント数 :', 'この動画にコメントはありません')
        # print('動画のURL :', 'https://www.youtube.com/watch?v=' + video_id)

        # 動画の再生回数順位
        video_ranking_number = ranking_number
        # 動画のID
        video_id = video_id
        # 動画のタイトル
        video_title = video_data['items'][0]['snippet']['title']
        # 動画の説明
        video_description = video_data['items'][0]['snippet']['description']
        # 動画の視聴回数
        video_viewCount = video_data['items'][0]['statistics']['viewCount']
        # 動画のアップデート日時
        video_publishedAt = video_data['items'][0]['snippet']['publishedAt']
        # 動画のサムネイル画像URL
        video_thumbnails_url = video_data['items'][0]['snippet']['thumbnails']['default']['url']
        # 動画の長さ
        video_duration = video_data['items'][0]['contentDetails']['duration']
        # 動画のキーワドタグ
        try :
            video_tags = video_data['items'][0]['snippet']['tags']
        except Exception as e:
            video_tags = 'この動画にキーワードタグはありません'
        # 動画のカテゴリID
        video_categoryId = video_data['items'][0]['snippet']['categoryId']
        # 動画の高評価数
        try:
            video_likeCount = video_data['items'][0]['statistics']['likeCount']
        except Exception as e:
            video_likeCount = 'この動画に動画の高評価数はありません'
        # 動画の低評価数
        try:
            video_dislikeCount = video_data['items'][0]['statistics']['dislikeCount']
        except Exception as e:
            video_dislikeCount = 'この動画に動画の低評価数はありません'
        # 動画のコメント数
        try:
            video_commentCount = video_data['items'][0]['statistics']['commentCount']
        except Exception as e:
            video_commentCount = 'この動画にコメントはありません'
        # 動画のURL
        video_rul = 'https://www.youtube.com/watch?v=' + video_id

        video_detail_dict = {
            'video_ranking_number':video_ranking_number,
            'video_id':video_id,
            'video_title':video_title,
            'video_description':video_description,
            'video_viewCount':video_viewCount,
            'video_publishedAt':video_publishedAt,
            'video_thumbnails_url':video_thumbnails_url,
            'video_duration':video_duration,
            'video_tags':video_tags,
            'video_categoryId':video_categoryId,
            'video_likeCount':video_likeCount,
            'video_dislikeCount':video_dislikeCount,
            'video_commentCount':video_commentCount,
            'video_rul':video_rul
        }

        print(video_detail_dict)

        





    return 0


if __name__ == "__main__":
    # 今のところおまじない
    my_part='snippet'
    # 検索キーワード
    my_q='ボードゲーム'
    # 視聴回数が多い順に取得
    my_order='viewCount'
    # 普通の動画から検索
    my_type='video'
    # 一度で取得できる件数(1-50件)
    my_num=6

    # ランキング順に動画IDを取得
    search_response, video_id_ranking_list = get_video_ranking(my_part=my_part, my_q=my_q, my_order=my_order, my_type=my_type, my_num=my_num)

    a = get_video_detail(video_id_ranking_list)
    
    # print(video_id_ranking_list)
