# ODIS Dashboard

This dashboard is meant to help monitor the Ocean Data and Information System (ODIS) graph.

# Docker steps

```
cd odis-arch/dashboard
docker build -t dashboard .
docker run --restart always -p 8501:8501 dashboard
```

# ODIS Documentation

Please see the ODIS Book, for getting started with 
your contributions: https://book.oceaninfohub.org/

# Contributions

We warmly encourage documentation contributions, even if it is a small error
or enhancement.  Please create a new pull request with your change.  Thank-you!

# License

See [LICENSE.md](LICENSE.md)