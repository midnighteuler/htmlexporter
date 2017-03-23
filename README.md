# htmlexporter
Jupyter notebook HTML export config and template with external resources (including CSS).

There's a custom preprocessor to export the embedded CSS into external files rather than within the HTML,
and it uses the ExtractOutputPreprocessor built into nbconvert.

Example use:
```
jupyter nbconvert --config=/path/to/htmlexport.py testnb.ipynb
```

The output folder is defined in the config file.
