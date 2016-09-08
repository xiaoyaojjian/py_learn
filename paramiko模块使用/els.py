from elasticsearch import Elasticsearch
#client = Elasticsearch()
es = Elasticsearch()
res=es.search(index="logstash-nginx-2016.05.23",
              doc_type="nginx_access",
              body={
   "query" : {
        "match" : {
           'httpcode':'404'
}
}
}
)
print (res)


