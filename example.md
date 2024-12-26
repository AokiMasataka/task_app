# このアプリはなにか？

Task管理するためのwebアプリケーション。

# モチベーション

- frontendの勉強したい
- どうせならwebアプリを作りたい
- ある程度役に立ちそうなものがいい

# 全体の構成
```mermaid
flowchart LR

US[User]

subgraph DC[Docker Compose]
    subgraph PG[PostgreSQL]
    end
    subgraph BE[Backend]
    end
    subgraph FE[Frontend]
    end
end

US --> FE
FE <--> BE
BE <--> PG

classDef DCC fill:none, color:#88d, stroke:#88d
class DC DCC
```

# 苦労 / 詰まったところ

- hogehoge

## 最初にやっておけばよかったこと

- 

# 今現在の課題

- フロントのデザインがコレジャナイ感ある...

# 今後やってみたいこと

- ログインシステムの追加
- Taskをまとめる "Project" 単位の導入
- kebenetesの導入