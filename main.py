import httpx
import asyncio
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich import box

# 	Discord:  9li2
# Want someone request Sites do follow bots for site samething add-me 
# // Privacy POLICY BOT HOSTING.NET RULES; 
# This  src code from bot-hosting.net this src code can used just for 1,2 trys so all. cookies, saves to domaim bot hosting after using the tool use proxy or VPN🔗 cause ip.auth doesnt get any warns
cookie = "YOUR COOKIE [ F12] "
auth_token = "AUTHTOKEN FROM APPLACTIONS OR UR NETWORK [F12] "
hcaptcha_response = "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQT3K3Q9OFZ3qZ1OCDcfqZA8sa9ZRvjG6wjcqWXYvCcVVGS0gC-KddVCvHxiH4Kdzb4oYbBMFRuAK82R_Jnlk2B6JliBQHMtNdIP6_prhRqN4jb7hgLxAffoPJfYTt0BSi-uXgc2g656PS0CYt8k7MxanTbZW_w5lfjxaQsS2AGmUKwqBaVBeCWKug0EgMY1LkJPd3aHsntePB7JVdaFR2kUFGsxjJ9a2VFqXfgq1Nc9f3zNlso5_qeIRCFqWVuUr7s7_aiT3_R7icAgQ9bSzo019cpAECfpCf0nqv0Xm3SnUs7qvA6SnUzhcYDrC9zsCZmI7t3Wkx6CZ0jAwBWa7SqtBpgUde-N8MI0jMcrqRkVORl2pGcbnV_fs9FL6NU7Pc7PwXj-dQHjpzgvoUbmmtY6xBHJDgAZyJsQ_zp4tvJ5q0RSNs2yZl25IxsxlKpqOjdfMyKQFLkOF1WS5DQba9e4uZdjKP5LwXOc7XWFnlutxdF_GG8yftTYlSmP-RmwdDO1J4Lca9o-Z7nx20JcskmtpwZX__yumiIu1GNI64TFNezV4ElNoY91i7iTtAz-p64IKg0wGJGLoZ50a9i5DVFVEtV45aW66M3rU0CRJy6AEkNq9vhzqNlBt-G1qkE3XAiBM8GqQEZwQKBezjt8XiNs03pvsN6K3vT9c1S4uBs0KmLurWFeTh-7nXBGqwTsjjioQqZK44ladFyQYJA5K4kIXPH24D3m8C3UJcV2jVr8F1WfYEbCT5JNnNx2hX7FLWc1i_Ga1j7GOun4MML2o7LYPkWj2-LzdE4cCJWJXVB2JwGshR4k6tT1veqoQ4bUB88UV3_2k76uwqoZQNl0KMfFgfsyodGKLpt8JwqhFlm6yvLSMbAD-k1kxHn0CRWRPOsRdoUiMi_3qvEsXu1kHOi8rcQg9GwFpny-l3jo2HdppkChzcShpqGQB3e3yX0YYqGYRS1CoUqp2HKHWyx0_7AYINKW_heFSZNyHb81Ac5yfMPsI3D4IOiBGDtX92fFah2isKL5IXOSMm_V-9moUdvNBhYGiv3FscsU4tKg6P_rMkaMsuyLxs5FE81Ulz_IvsrXYnrJkWWz2HR-i_U3lt0ov39NrC56qEWyvcVgYSddn0N0CQa7GXjykWMOErvVvcS9SA6z8Niq5WxWE_-lMs7ttE8yqMZuxzByrE0h9xG6pL-Zvx6Fuuo9tY1D87unTc07AU0hREymhfts-03OAEpUNHhshSvQozpbizC_-sKVBxl3Z8O0JQHWz5gerlqNyIvUtCf7RVrkHVpHGi5pSXgUL8Wp9dQ06lcEGir0K2ofcsq9PmcsaA-ADzErpIEf1Gy199KIrYb3IYKl4YWOCbRWvlZJyznCoIQ7tO50O-a1B3ONOGeWg1ACr2sFNpw7yRM3UDtEoa66m4smKtOhs75podDCGP4GbrwiUyyXVInkuKvPccRS1HmXi0wkkzx8Pa1tioKweYZ0RcvzSGTPnvp7O9FndDbnPsZPI6Nyqkzq4X6uA3ByItIoKMUJHmVQXDv8zKNBaW8fPT4S6UxthNhnUcIxWBxKg0G95KseCBC1RXETmqTQeIch9HDlDSMe7yV40wdv-CX0iGnFAfJpfFKg_41sGQ0X1WZZtOAwyjUZG-jQQEBbxIwWZOaYDz1FJXIogbxp7Mf0rF80yylwC4KfcPdZWAZ1FZejZXhwzmcnxPCoc2hhcmRfaWTOAzGDb6Jrcqg0MzhjMWIxNaJwZAA.rY9Bwz_cryII5IVvOjGnD05xQULCcB6Z6W_gSZu6FYk" # Hcaptcha solver Dont remove it😭


headers = {
    "authority": "bot-hosting.net",
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": auth_token,
    "content-type": "application/json",
    "cookie": cookie,
    "origin": "https://bot-hosting.net",
    "referer": "https://bot-hosting.net/panel/earn",
    "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
    "sec-ch-ua-arch": "",
    "sec-ch-ua-bitness": "",
    "sec-ch-ua-full-version": "124.0.6327.4",
    "sec-ch-ua-full-version-list": '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-model": "SM-A235F",
    "sec-ch-ua-platform": "Android",
    "sec-ch-ua-platform-version": "14.0.0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
}


payload = {
    "hCaptchaResponse": hcaptcha_response
}


success_count = 0
failure_count = 0


console = Console()
table = Table(title="Request Status - SERVER CONNECTED", box=box.ROUNDED, show_edge=False, show_header=True, header_style="bold blue")
table.add_column("NO PROXY 🔥", style="yellow", justify="center")
table.add_column("Request 🔥#", style="cyan", justify="center")
table.add_column("Status🔥", style="green", justify="center")
table.add_column("Message🔥", style="magenta", justify="center")

async def send_request(session, req_number):
    global success_count, failure_count
    led_icon = "💡"  # playersearch:="1234"
    try:
        response = await session.post(
            'https://bot-hosting.net/api/freeCoins',
            headers=headers,
            json=payload
        )
        if response.status_code == 200:
            success_count += 1
            led_text = Text(f"{led_icon} ON", style="bold green")
            table.add_row(led_text, str(req_number), "Success", "✅ Coins Received")
        else:
            failure_count += 1
            led_text = Text(f"{led_icon} OFF", style="bold red")
            table.add_row(led_text, str(req_number), "Failed", f"⚠️ Status Code: {response.status_code}")
    except Exception as e:
        failure_count += 1
        led_text = Text(f"{led_icon} OFF", style="bold red")
        table.add_row(led_text, str(req_number), "Failed", f"⚠️ Error: {str(e)}")

async def main():
    async with httpx.AsyncClient() as session:
        tasks = [send_request(session, i + 1) for i in range(100)]
        with Live(table, console=console, refresh_per_second=4, transient=True):
            await asyncio.gather(*tasks)

  
    summary_panel = Panel(
        f"[bold green]Success Requests:[/bold green] [green]{success_count}[/green]  "
        f"[bold red]Failed Requests:[/bold red] [red]{failure_count}[/red]",
        title="Results : === XYZ DISCORD THEN 9li2 dont forget this tool should'nt be share in public  in normally is for sell💰",
        style="bold magenta",
        border_style="bright_yellow"
    )
    console.print(summary_panel)


asyncio.run(main())
