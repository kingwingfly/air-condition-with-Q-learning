Python Reproduction of [A reinforcement learning-enabled iterative learning control strategy of
air-conditioning systems for building energy saving by shortening the morning start period](https://doi.org/10.1016/j.apenergy.2023.120650).

# Usage

Modify the `src/config.py` to change the configuration.

```sh
uv run src/main.py
```

# Conclusion

As I reading the article, I found the state choosing is totally wrong. 
And its simulation is actually fake which shows improvement on the sys 
with only 3 updates while 15 Q-values in total. 
