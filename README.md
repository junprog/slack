# slack
Incoming Webhook を利用したコードです

Qiita記事は [こちら](https://qiita.com/vip-J/items/af12e3331629800dc73e)

# 構築

コードを持ってくる。
```shell
$ cd ~/Documents
$ git clone git@github.com:junprog/slack.git
```

PATHを通す。
```shell
$ echo export "PATH=$HOME/Documents/slack:$PATH" >> ~/.bash_profile
$ source ~/.bash_profile
$ echo alias aoi='bash watch' >> ~/.bash_aliases
$ source  ~/.bash_aliases
```

# 実行

```shell
$ aoi [PID]
```