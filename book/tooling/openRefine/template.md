# Template

## About

The following are the templates sections for the OpenRefine
export template command.

There are four sections



## PREFIX

``` 
{
    "@context": "https://schema.org",
    "@type": ["ItemList", "CreativeWork"],
    "name": "Top 5 covers of Bob Dylan Songs",
    "author": "John Doe",
    "about": {
      "@type": "Course"
    },
    "itemListElement": [

```

## ROW TEMPLATE

``` 
{
    "@context": {
        "@vocab": "https://schema.org/",
        "endDate": {
            "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "startDate": {
            "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        }
    },
    "@id":  {{jsonize(cells["ID"].value)}},
    "@type":{{jsonize(cells["type"].value)}},
    "description":  {{jsonize(cells["description"].value)}},
    "name" : {{jsonize(cells["name"].value)}},
    "hasCourseInstance": {
        "@type":  {{jsonize(cells["CourseInstance"].value)}},
        "courseMode":  {{jsonize(cells["courseMode"].value)}},
        "endDate":  {{jsonize(cells["enddata"].value)}},
        "startDate":{{jsonize(cells["startdate"].value)}}
    },
    "provider": {
        "@type": "CollegeOrUniversity",
        "name": {{jsonize(cells["provider.name"].value)}},
        "url": {
            "@id":  {{jsonize(cells["provider.url"].value)}}
        }
    }
}

```

## ROW SEP

``` 
,
```


## SUFFIX

``` 
 ]
}
```

## NOTES

``` 


{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Course",
    "courseCode": "F300",
    "name": "Physics",
    "provider": {
        "@type": "CollegeOrUniversity",
        "name": "University of Bristol",
        "url": {
            "@id": "/provider/324/university-of-bristol"
        }
    }
}


    {
      "ID" : {{jsonize(cells["ID"].value)}},
      "type" : {{jsonize(cells["type"].value)}},
      "description" : {{jsonize(cells["description"].value)}},
      "name" : {{jsonize(cells["name"].value)}},
      "provider.name" : {{jsonize(cells["provider.name"].value)}},
      "provider.url" : {{jsonize(cells["provider.url"].value)}},
      "CourseInstance" : {{jsonize(cells["CourseInstance"].value)}},
      "courseMode" : {{jsonize(cells["courseMode"].value)}},
      "enddata" : {{jsonize(cells["enddata"].value)}},
      "startdate" : {{jsonize(cells["startdate"].value)}}
    }


```
