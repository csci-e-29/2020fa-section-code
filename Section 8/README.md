# Section 8 - Dask

### Agenda:
- Dask examples


##### CudaDF commands
Setup is found [here](https://rapids.ai/start.html)

```
docker pull rapidsai/rapidsai:cuda10.1-runtime-ubuntu18.04
docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai:cuda10.1-runtime-ubuntu18.04
```

### Key points/notes:

Dask: 

    Dask is a flexible library for parallel computing in Python. Core components include:

    COLLECTIONS: Objects like Dask Arrays, Dataframes, Bags, etc.

    TASK GRAPH: Symbolically create a delayed computational graph

    SCHEDULERS: Runs on single-machines via threads/processes and runs distributed as well
    
    Most operations are delayed, i.e. they operate lazily. Functions are not automatically executed, but deferred as much as possible. Note that the call delayed on the function, not the result.
    Avoid calling compute repeatedly -- the idea is to call compute after you've finished building your graph.
    
Dask Dataframes: 
    
    Dask dataframes can be thought of as many chunked pandas dataframe. The API is very similar to that of pandas, for example you can do
    
    import dask.dataframe as dd
    dd.read_csv("some_file.csv")
    
    Transform a dask dataframe back into a pandas dataframe by calling compute (note -- very rarely should you do this!)
    
    dask_df.compute()
    
    The functions you know and love also work as well:
    
    df.groupby('name').x.mean().compute()
    
    Not all pandas operations are supported, but for those you can use map partitions instead, which is similar to doing apply on a pandas DataFrame:
    
    ddf.map_partitions(lambda df: df.assign(z=df.x * df.y))
    
    https://docs.dask.org/en/latest/dataframe.html

Other useful Dask components: 
    
    Dask supports many data science applications, including hyperparameter tuning, GLMs, SVD, XGBoost, etc.
    https://examples.dask.org/machine-learning/scale-scikit-learn.html 
     
    Dask supports distributed computing in Python.
    https://distributed.dask.org/en/latest/
    
Parquet:
    
    Parquet is an open source file format designed for flat columnar storage.
    
    COLUMNAR STORAGE: stores data by columns rather than rows
    
    Some benefits include allowing column-wise operations to be applied quickly, compression to reduce storage space, and metadata about each row group to be stored. 