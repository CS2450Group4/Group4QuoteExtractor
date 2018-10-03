from newspaper import Article

#Singleton class with the method extractArticleText
class ArticleExtractor:

    #extractArticleText: Recieves URL as string and returns the article found at the URL's webpage as a string
    def extractArticleText(urlString):
        url = urlString

        article = Article(url)

        print("Downloading webpage...")

        article.download()

        print("Pulling article from webpage...")

        article.parse()

        return article.text




