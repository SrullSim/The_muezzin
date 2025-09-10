# The_muezzin


    -   env - config dir

    -   data store in data dir 

    -   loader load the data and publish them through kafka in controller.py

    -   subscriber in processor dir get the data and use tools in a different directories..

    -   in elastic dir uoy can find the connection and crud actions 
        and above them dal who powered by process as mentioned 

    -   also powered by processor its the mongo Dal from mongo directory 
            use to store there the content of the files.
            i used gridFS lib for binary data

    -   also added function to convert the speech to text ('STT') using the speech_recognition library,
            it happened inside the consumer loop, before insert the doc to index of elastic search.
            I choose to do it before sending to elastic in the first place just for save processing power,
            even that its take more time.


now I about to analys the text we just extract, first I gonna clan it from stop words, Punctuation marks, Linking words
    while I'm during it, I was thinking, of course in Operational system the data should upload 
    immediately  to somewhere and then analys it, and that I should do, but for start i  did somthing else
    and after I will finish I'will update it, so for now it happened before upload do elastic in the first place,
    temporary !.
    i choose to rate the danger by dangerous words in the text(podcast), comper to all the words,
    rate lower than 0.10% count not dangerous,
    rate between 0.10% to 0.20% count like medium dangerous,
    rate above 0.20% count like very dangerous,
    and for the very dangerous words, I calculate different...
    -   each document have score who combine the danger rate of both words lists
        -   for dangerous words I'm dividing the sum of dangerous words by sum of all the words in the current text
        -   for the very dangerous words again dividing  the sum of them by the len of the general text
                but just before combine them to a final score multiply the result and then add them together.
                that go to field bds_percent 
        -   according the result in this field we can tell how danger the content inside. 
            I decided that content with more than 0.12% of it it's dangerous words the danger cant by inadvertently, 
            so that one we can say should be category in danger=true.
            * of course it's just for cases that the percent will be less than medium treat level but we can say 
            that inside are we can say with certainty that there is danger in the content of this text.




    - the process is: 
        *  _id pushed into mongodb while the data pushed with GriFS to differet collection

        *  i pull from GridFS collection the content of the current podcast by hes _id
            
            read the binary content and use function in cnsumer class to convert it to text.
            
            add the content to the dict who send to index one by one in loop until the event finished.
        
        *   in part 4 added analyser comper the content to list of words and store into elastic index the 
                
            the conclusions according to the requirements.  
        
        *   all the process hppened before sending to elastic, 
            and as mentioned i know and I gonna change it after. !! I would appreciate your consideration of the situation.







commands :
    
[//]: # (    docker compose for all the containers). "recommended !!"
    -  docker compose up -d

[//]: # (    to run kibana container )
    - docker run -d --name kibana -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://localhost:9200/" `docker.elastic.co/kibana/kibana:9.1.0

[//]: #  ( for run elasticsearch container )
    - docker run -d --name kibana --network elastic-net -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://localhost:9200/" `docker.elastic.co/kibana/kibana:9.1.0

[//]: # ( docker )
    - docker build -t poducer-muazin:0.1 -f Dockerfile_consumer .

    -  docker build -t consumer-muazin:0.1 -f Dockerfile_producer .

    -   docker run -d --name muazin --network muazin-network producer-muazin:0.1 

    -   docker run -d --name muazin --network muazin-network consumer-muazin:0.1 
