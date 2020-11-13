# Services

## References


## Vocabulary resources


## Metadata elements of interest


## Notes


* https://schema.org/docs/actions.html
* https://schema.org/Action
* https://www.w3.org/TR/web-share/
* https://www.hydra-cg.com/spec/latest/core/

The graph describes a service than can be invoked with

```bash
curl --data-binary "@yourfile.jpg" -X POST https://us-central1-top-operand-112611.cloudfunctions.net/function-1
```

This with POST a jpeg to the service and get back a simple text response with some information 
about the image.

```json
{
  "@context": "http://schema.org/",
  "@type": "Action",
  "@id": "https://us-central1-top-operand-112611.cloudfunctions.net/function-1",
  "result": {
    "@type": "DataDownload",
    "encodingFormat": "text/plain",
    "description": "a simple text result for the RGB counts"
  },
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://us-central1-top-operand-112611.cloudfunctions.net/function-1",
    "httpMethod": "POST",
    "contentType": ["image/jpeg", "image/png"]
  },
  "object": {
    "@type": "ImageObject",
    "description": "A JPEG or PNG to analyze the RGB counts"
  }
}
```