import requests

class GoogleSearch:
    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id 
    
    def search(self, query, start_page=1, pages=1, lang="es"):
        final_results = []
        results_per_page = 10 #google muestra 10 resultados por pagina
        for page in range(pages):
            start_index = (start_page - 1 ) * results_per_page + 1 + (page * results_per_page)
        url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.search_engine_id}&q={query}&start={start_index}&lr={lang}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get("items")
            cresults = self.custom_results(results)
            final_results.extend(cresults)
        else:
            print("Error in request")
            
        return final_results
        


    def custom_results(self, results):
        custom_results = []
        for r in results:
            cresult ={}
            cresult["title"] = r.get("title")
            cresult["description"] = r.get("snippet")
            cresult["link"] = r.get("link")
            custom_results.append(cresult)
        return custom_results