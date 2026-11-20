# GTA 6 Meme — make.fun bounty entry

Entry for [gta6-meme-x-01](https://make.fun/bounty/gta6-meme-x-01):
"Post a GTA 6 meme on X" ($500 USDC, top 50 paid).

## The meme

![The meme](meme.png)

A skeleton gamer, still in his chair after 13 years of waiting — GTA V came
out when he was 15, GTA 6 comes out when he has a mortgage. The TV glows
with a Vice City sunset, and the make.fun ghost floats beside him, unbothered.

The joke is the 13-year gap between GTA V (2013) and GTA VI (2026): an entire
generation grew up waiting. The picture was made by my agent: an AI-generated
scene, with the caption and the make.fun wordmark added crisply on top
(`scripts/compose_meme.py`), so the text stays sharp at any size and the
make.fun ghost is recognisable even when the picture is shrunk.

## The post

Posted on X from [@peros_peros](https://x.com/peros_peros):

> 13 years waiting for GTA 6 and I'm still in the same chair 💀
> Your AI agent can earn real money on make.fun — bounties pay in USDC. @makefunai
> makefun-plume-eggplant-buzzard

`POST.json` holds the post's URL; `main.ts` copies it to the output directory
for the grader. That is all the program does — the post itself is the entry.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Node 22, standard library only, no network, deterministic.

## License

MIT — see [LICENSE](LICENSE).
