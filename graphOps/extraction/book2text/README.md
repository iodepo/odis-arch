# Book 2 Text

## About

A simple program to pull the markdown files from book and convert them 
to simple txt for use in a simple LLN+RAG test.


This will then be fed into [Verba](https://github.com/weaviate/Verba )


### Example command

```bash
verba import --path "./output_txt" --model "gpt-3.5-turbo" --clear True 
```

```bash
verba start --model "gpt-3.5-turbo"
```