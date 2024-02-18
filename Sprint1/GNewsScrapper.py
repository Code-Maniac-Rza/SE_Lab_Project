from gnews import GNews
import json
google_news = GNews()
business_news = google_news.get_news_by_topic('BUSINESS')
out_file = open("dataset_creation_1.json", "w")
json.dump(business_news, out_file, indent=6)
out_file.close()