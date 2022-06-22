## Offline documentation server.

Project in development.

This is a python package created for serving documentions of diferents technologies and programing languages. When it start all it does is creating an http server on differents threads each. The documentation are a static websites, made from the official github repository.

### How to use it.

1. `pip install doc_server`
2. `doc_server` To start the servers
    * `doc_server -d path_docs_folder` To change the docs folder, default `~/.doc_server_docs` 
    * `doc_server -a zip_to_add` Add a new doc to the docs folder
    * `doc_server --help` To visualize the help