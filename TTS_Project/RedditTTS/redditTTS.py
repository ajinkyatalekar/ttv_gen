import praw
from gtts import gTTS

class RedditTTS:
    reddit = None

    def create(self):
        global reddit
        reddit = praw.Reddit(
                    client_id='',
                    client_secret='',
                    user_agent="ttvGenerator"
                )

    def getFromURL(self,url):
        ret = {}
        if '/comment/' in url:
            item = reddit.comment(url=url)
            
            ret['type'] = 'comment'
            ret['body'] = item.body
            ret['author'] = item.author
        else:
            item = reddit.submission(url=url)

            ret['type'] = 'post'
            ret['title'] = item.title
            ret['selftext'] = item.selftext
            ret['author'] = item.author
        return ret

    def generate(self,queue):
        genAudio(queue)

    def genAudio(self, queue):
        for sub in queue:

            if sub['type'] == 'post':
                audioString = ''
                audioString += sub['title'] + "."
                audioString += sub['selftext'] + "."

                aud = gTTS(text=audioString, lang='en', slow=False, tld='ca')

                path = app_path+'/temp/' + sub['id']
                if not os.path.exists(path):
                    os.makedirs(path)

                aud.save(app_path+'/temp/' + sub['id'] + '/tts.mp3')
            else:
                aud = gTTS(text=comment['body']+'.', lang='en', slow=False, tld='ca')
                aud.save(app_path+'/temp/' + sub['id'] + '/' + str(i) + 'com.mp3')
                i = i+1
