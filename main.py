from fasthtml.common import *
from starlette.staticfiles import StaticFiles
from mangum import Mangum
import os

# ── App setup ─────────────────────────────────────────────────

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23000'/%3E%3Ctext x='16' y='23' font-family='monospace' font-weight='900' font-size='18' fill='%23cc0000' text-anchor='middle'%3ESS%3C/text%3E%3C/svg%3E"

_fh, rt = fast_app(
    hdrs=(
        Meta(name="theme-color", content="#cc0000"),
        Link(rel="icon", href=FAVICON),
        Meta(property="og:title", content="SastaSentinels | Elite Esports Squad"),
        Meta(property="og:description", content="SastaSentinels — seven friends, one squad, zero mercy. FPS and beyond."),
        Meta(property="og:type", content="website"),
        Meta(name="twitter:card", content="summary"),
        Meta(name="twitter:title", content="SastaSentinels | Elite Esports Squad"),
        Meta(name="twitter:description", content="SastaSentinels — seven friends, one squad, zero mercy. FPS and beyond."),
        Link(rel="dns-prefetch", href="https://media.valorant-api.com"),
        Link(rel="preconnect", href="https://media.valorant-api.com", crossorigin=""),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap"),
        Link(rel="stylesheet", href="/static/style.css"),
        Script(src="/_vercel/insights/script.js", defer=True),
        Script(src="/_vercel/speed-insights/script.js", defer=True),
    ),
    live=False,
)

# Explicit simple assignment — required for Vercel's AST scanner
app = _fh

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# ── Data ──────────────────────────────────────────────────────

PLAYERS = [
    dict(ign="BeastM0del",   name="Arpan Bose",             role="CARRY · TOP FRAGGER",  num="07", initials="AB", ace=True,
         bio="The squad's undisputed ace. BeastM0del operates on a level the rest of us are still chasing — the player enemies study in VODs, teammates rally behind, and opponents dread seeing in the lobby.",
         agent="add6443a-41bd-e414-f6ad-e58d267f4e95"),
    dict(ign="WizVoltric",   name="Nikhar Mahendra Singh",  role="CO-IGL · RIFLER",       num="01", initials="WV", ace=False,
         bio="Electric reflexes and relentless aggression. WizVoltric sets the pace on the server — a rifler who makes space, wins duels, and executes the calls that GreyWolf crafts.",
         agent="569fdd95-4d10-43ab-ca70-79becc718b46"),
    dict(ign="GreyWolf",     name="Aditya Kumar Singh",     role="HEAD IGL · STRATEGIST", num="02", initials="GW", ace=False,
         bio="The mind the squad runs on. GreyWolf's reads are a round ahead of everyone else — dissecting enemy patterns mid-game and calling the plays that turn losing maps into clean wins.",
         agent="22697a3d-45bf-8dd7-4fec-84a9e28c69d7"),
    dict(ign="KINGPIN",      name="Debraj Burman",          role="ENTRY FRAGGER",         num="03", initials="KP", ace=False,
         bio="Fear is a foreign concept. Leads the charge every round, forcing duels with terrifying confidence and setting the relentless pace that defines every round's outcome.",
         agent="f94c3b30-42be-e959-889c-5aa313dba261"),
    dict(ign="Sectumsempra", name="Kartikeya Singh",        role="AWPer · SNIPER",        num="04", initials="SS", ace=False,
         bio="Long angles don't exist — only targets. One flick, one bullet, one soul less on the enemy roster per round. Crosshair placement is a spell in itself.",
         agent="a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"),
    dict(ign="AgentTrigger", name="Arpan Mitra",            role="SUPPORT · CLUTCH",      num="05", initials="AT", ace=False,
         bio="When rounds seem lost and teammates are down, AgentTrigger triggers. Maestro of utility, ghost of 1vX situations, and the sole reason comebacks even happen.",
         agent="0e38b510-41a8-5780-5e8f-568b2a4f2d6c"),
    dict(ign="STING",        name="Kaushik",                role="SENTINEL · ANCHOR",     num="06", initials="ST", ace=False,
         bio="Sites don't fall while STING holds them. A fortress of discipline and game sense, anchoring defenses with patience that turns every aggression into a free kill.",
         agent="8e253930-4c05-31dd-1b6c-968525494517"),
]

MATCHES = [
    dict(result="WIN",  game="VALORANT", map_name="Ascent",       score="13 – 7",    mode="Competitive", date="Apr 2025"),
    dict(result="LOSS", game="VALORANT", map_name="Bind",         score="10 – 13",   mode="Competitive", date="Apr 2025"),
    dict(result="WIN",  game="CS2",      map_name="Dust II",      score="16 – 9",    mode="Matchmaking",  date="Mar 2025"),
    dict(result="WIN",  game="VALORANT", map_name="Haven",        score="13 – 5",    mode="Competitive", date="Mar 2025"),
    dict(result="LOSS", game="APEX",     map_name="Kings Canyon", score="2nd Place", mode="Ranked BR",   date="Feb 2025"),
]

FPS_GAMES = [
    dict(code="VAL",  name="Valorant",         fill=95, badge="MAIN",    featured=True,
         desc="Our primary battleground. Agents, angles, and abilities — we master every meta shift."),
    dict(code="CS2",  name="Counter-Strike 2", fill=80, badge="CLASSIC", featured=False,
         desc="The foundation of all tactical shooters. We pay our respects and sharpen fundamentals here."),
    dict(code="APEX", name="Apex Legends",     fill=72, badge="BR",      featured=False,
         desc="Movement mechanics that punish the lazy and reward the mechanically gifted."),
    dict(code="WZ",   name="Warzone",          fill=65, badge="BR",      featured=False,
         desc="Drop hot. Loot fast. Dominate the final circle. We don't survive — we hunt."),
]

STORY_GAMES = [
    dict(code="GoW",  name="God of War",  desc="Kratos humbles us every time. A masterclass in storytelling."),
    dict(code="RDR2", name="Red Dead 2",  desc="When we need to appreciate an open world built with obsessive detail."),
    dict(code="TLOU", name="Last of Us",  desc="Survival, emotion, impossible choices. No one walks away unchanged."),
    dict(code="GTA",  name="GTA V",       desc="Off-duty chaos and creative destruction. Sometimes you just vibe."),
]


# ── SVG icons ─────────────────────────────────────────────────

def yt_svg():
    return NotStr('<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>')

def dc_svg():
    return NotStr('<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057.101 18.06.105 18.071.112 18.082a19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>')

def ig_svg():
    return NotStr('<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>')

def tw_svg():
    return NotStr('<svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>')

def sound_off_svg():
    return NotStr('<svg class="sound-icon sound-off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>')

def sound_on_svg():
    return NotStr('<svg class="sound-icon sound-on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14" style="display:none"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>')


# ── Section components ────────────────────────────────────────

def crosshair_el():
    return Div(
        Div(cls="ch-arm top"), Div(cls="ch-arm bot"),
        Div(cls="ch-arm lft"), Div(cls="ch-arm rgt"),
        id="crosshair",
    )

def splash_el():
    return Div(
        Div(cls="splash-scanline"),
        Div(
            Span(cls="hc tl"), Span(cls="hc tr"),
            Span(cls="hc bl"), Span(cls="hc br"),
            Div(Span("[", cls="sl-b"), Span("SS", cls="sl-i"), Span("]", cls="sl-b"), cls="splash-logo"),
            Div(Span("SASTA", cls="sw-a"), Span("SENTINELS", cls="sw-b"), cls="splash-wordmark"),
            Div(cls="splash-sep"),
            Div(Div(cls="splash-fill"), cls="splash-track"),
            P("INITIALIZING...", cls="splash-status", id="splashStatus"),
            cls="splash-hud",
        ),
        id="splash",
    )

def navbar_el():
    return Nav(
        Div(
            A(Span("[", cls="logo-bracket"), Span("SS", cls="logo-text"), Span("]", cls="logo-bracket"),
              href="#hero", cls="nav-logo"),
            Ul(
                Li(A("Home",       href="#hero")),
                Li(A("Squad",      href="#team")),
                Li(A("Arsenal",    href="#games")),
                Li(A("Highlights", href="#highlights")),
                cls="nav-links", id="navLinks",
            ),
            Div(
                Div(Span(cls="status-dot"), Span("ACTIVE"), cls="nav-status"),
                Button(sound_off_svg(), sound_on_svg(),
                       cls="sound-toggle", id="soundToggle", aria_label="Toggle sound effects"),
                Button(Span(), Span(), Span(), cls="hamburger", id="hamburger", aria_label="Menu"),
                cls="nav-right",
            ),
            cls="nav-container",
        ),
        id="navbar",
    )

def mobile_menu_el():
    return Div(
        Ul(
            Li(A("Home",       href="#hero",       cls="mobile-link")),
            Li(A("Squad",      href="#team",       cls="mobile-link")),
            Li(A("Arsenal",    href="#games",      cls="mobile-link")),
            Li(A("Highlights", href="#highlights", cls="mobile-link")),
        ),
        cls="mobile-menu", id="mobileMenu",
    )

def hero_el():
    return Section(
        Canvas(id="heroCanvas"),
        Div(cls="hero-overlay"),
        Div(
            Div("// ELITE ESPORTS SQUAD", cls="hero-tag"),
            H1(
                Span("SASTA", cls="title-sasta glitch", data_text="SASTA"),
                Span("SENTINELS", cls="title-sentinels"),
                cls="hero-title",
            ),
            P(cls="hero-tagline", id="tagline"),
            Div(
                Div(Span("7", cls="stat-number"), Span("PLAYERS",    cls="stat-label"), cls="stat"),
                Div(cls="stat-divider"),
                Div(Span("∞", cls="stat-number"), Span("DEDICATION", cls="stat-label"), cls="stat"),
                Div(cls="stat-divider"),
                Div(Span("1", cls="stat-number"), Span("SQUAD",      cls="stat-label"), cls="stat"),
                cls="hero-stats",
            ),
            A(Span("MEET THE SQUAD"), Span("↓", cls="cta-arrow"), href="#team", cls="hero-cta"),
            cls="hero-content",
        ),
        Div(cls="hero-scroll-line"),
        id="hero",
    )

def stats_el():
    items = [("1200", "+", "HOURS PLAYED"), ("340", "+", "MATCHES"), ("7", "", "PLAYERS"), ("4", "+", "GAMES MASTERED")]
    blocks = []
    for i, (target, unit, label) in enumerate(items):
        blocks.append(Div(
            Div(
                Span("0", cls="stat-counter-num", data_target=target),
                Span(unit, cls="stat-unit") if unit else "",
                cls="stat-num-row",
            ),
            Span(label, cls="stat-desc"),
            cls="stat-block",
        ))
        if i < len(items) - 1:
            blocks.append(Div(cls="stats-sep"))
    return Section(Div(*blocks, cls="stats-banner"), id="stats")

def quote_el():
    return Section(
        Div(cls="quote-bg"),
        Div(
            Div(cls="quote-line"),
            Blockquote(
                '"We don\'t play to participate.',
                Br(),
                Span("We play to obliterate.", cls="quote-accent"),
                '"',
                cls="quote-text",
            ),
            P("— SASTA SENTINELS", cls="quote-attr"),
            Div(cls="quote-line"),
            cls="quote-content",
        ),
        id="quote",
    )

def player_card_el(p):
    ace = p["ace"]
    corners = [Div(cls=f"card-corner {pos}") for pos in ("tl", "tr", "bl", "br")]
    badge = [Div("★ THE PRO", cls="ace-badge")] if ace else []
    return Div(
        Div(cls="card-border-glow"),
        Div(
            *corners,
            *badge,
            Span(f"#{p['num']}", cls="card-num-bg"),
            Div(
                Div(cls="avatar-ring" + (" ace-ring" if ace else "")),
                Div(p["initials"], cls="avatar-core" + (" ace-core" if ace else "")),
                Span(f"#{p['num']}", cls="avatar-num"),
                cls="player-avatar",
            ),
            Div(
                Div(p["role"], cls="player-role" + (" ace-role" if ace else "")),
                H3(p["ign"], cls="player-ign"),
                P(p["name"], cls="player-realname"),
                P(p["bio"], cls="player-bio"),
                cls="player-info",
            ),
            cls="card-inner",
        ),
        cls="player-card" + (" ace-card" if ace else ""),
    )

def team_el():
    return Section(
        Div(
            Div(
                Span("// THE SQUAD", cls="section-tag"),
                H2("MEET THE ", Span("SENTINELS", cls="accent"), cls="section-title"),
                P("Seven players. One purpose. Zero mercy.", cls="section-subtitle"),
                cls="section-header",
            ),
            Div(*[player_card_el(p) for p in PLAYERS], cls="team-grid"),
            cls="section-container",
        ),
        id="team",
    )

def match_row_el(m):
    r = m["result"].lower()
    return Div(
        Span(m["result"], cls=f"match-result-badge {r}"),
        Div(Span(m["game"], cls="match-game"), Span(m["map_name"], cls="match-map"), cls="match-meta"),
        Span(m["score"], cls="match-score"),
        Span(m["mode"],  cls="match-mode"),
        Span(m["date"],  cls="match-date"),
        cls=f"match-row {r}",
    )

def matches_el():
    return Section(
        Div(
            Div(
                Span("// RECENT ACTIVITY", cls="section-tag"),
                H2("MATCH ", Span("HISTORY", cls="accent"), cls="section-title"),
                P("Last recorded sessions across competitive playlists.", cls="section-subtitle"),
                cls="section-header",
            ),
            Div(*[match_row_el(m) for m in MATCHES], cls="match-list"),
            cls="section-container",
        ),
        id="matches",
    )

def fps_card_el(g):
    return Div(
        Div(g["badge"], cls="game-badge" + ("" if g["featured"] else " dim")),
        Div(g["code"], cls="game-code"),
        H4(g["name"], cls="game-name"),
        P(g["desc"],  cls="game-desc"),
        Div(Div(cls="game-bar-fill", data_fill=str(g["fill"])), cls="game-bar"),
        cls="game-card" + (" featured" if g["featured"] else ""),
    )

def story_card_el(g):
    return Div(
        Div(g["code"], cls="game-code sm"),
        H4(g["name"], cls="game-name"),
        P(g["desc"],  cls="game-desc"),
        cls="game-card story",
    )

def games_el():
    return Section(
        Div(
            Div(
                Span("// ARSENAL", cls="section-tag"),
                H2("GAMES WE ", Span("PLAY", cls="accent"), cls="section-title"),
                P("From tactical FPS to epic narratives — we play it all.", cls="section-subtitle"),
                cls="section-header",
            ),
            Div(
                Div(Span("⊕", cls="cat-icon"), Span("COMPETITIVE FPS"), Div(cls="cat-line"), cls="category-label"),
                Div(*[fps_card_el(g) for g in FPS_GAMES], cls="fps-grid"),
                cls="games-category",
            ),
            Div(
                Div(Span("◈", cls="cat-icon"), Span("STORY & ADVENTURE"), Div(cls="cat-line"), cls="category-label"),
                Div(*[story_card_el(g) for g in STORY_GAMES], cls="story-grid"),
                cls="games-category",
            ),
            cls="section-container",
        ),
        id="games",
    )

def highlights_el():
    clips = [
        Div(
            Div(
                Span("▶", cls="ph-icon"),
                Span(f"HIGHLIGHT CLIP · 0{i+1}", cls="ph-text"),
                Span("youtube.com/@wizly25/streams", cls="ph-sub"),
                cls="highlight-placeholder",
            ),
            cls="highlight-wrap", data_video=f"VIDEO_ID_{i+1}",
        )
        for i in range(3)
    ]
    return Section(
        Div(
            Div(
                Span("// CONTENT", cls="section-tag"),
                H2("HIGHLIGHTS & ", Span("CLIPS", cls="accent"), cls="section-title"),
                P("Watch us in action — raw gameplay, clutch moments, zero filter.", cls="section-subtitle"),
                cls="section-header",
            ),
            Div(*clips, cls="highlights-grid"),
            Div(
                A(Span("▶", cls="yt-icon"), Span("VIEW ALL ON YOUTUBE"),
                  href="https://www.youtube.com/@wizly25/streams",
                  target="_blank", rel="noopener", cls="yt-link"),
                cls="highlights-cta",
            ),
            cls="section-container",
        ),
        id="highlights",
    )

def join_el():
    reqs = [
        "Diamond rank or equivalent mechanical ability",
        "Consistent availability for scheduled sessions",
        "Team-first mindset — ego stays at the lobby screen",
        "Vouched in by an existing member",
    ]
    return Section(
        Div("SENTINEL", cls="join-bg-text"),
        Div(
            Span("// MEMBERSHIP", cls="section-tag",
                 style="display:block;text-align:center;margin-bottom:1.5rem;"),
            H2("WE DON'T RECRUIT.", Br(), Span("WE RECOGNISE.", cls="accent"), cls="join-title"),
            P("SastaSentinels isn't something you apply for — it's something you earn through game sense, team play, and an undying will to win. If you can keep up, you already know who you are.",
              cls="join-desc"),
            Div(*[Div(Span("▸", cls="req-icon"), Span(r), cls="req-item") for r in reqs], cls="join-reqs"),
            A(Span("WATCH US FIRST"),
              href="https://www.youtube.com/@wizly25", target="_blank", rel="noopener", cls="join-btn"),
            cls="join-inner",
        ),
        id="join",
    )

def footer_el():
    return Footer(
        Div(
            Div(Span("[", cls="logo-bracket"), Span("SASTA SENTINELS", cls="logo-text"), Span("]", cls="logo-bracket"),
                cls="footer-logo"),
            P("WE AIM · WE CONQUER · WE DOMINATE", cls="footer-tagline"),
            Div(
                A(yt_svg(), Span("YouTube"),     href="https://www.youtube.com/@wizly25", target="_blank", rel="noopener", cls="social-link", aria_label="YouTube"),
                A(dc_svg(), Span("Discord"),     href="#", cls="social-link", aria_label="Discord"),
                A(ig_svg(), Span("Instagram"),   href="#", cls="social-link", aria_label="Instagram"),
                A(tw_svg(), Span("Twitter / X"), href="#", cls="social-link", aria_label="Twitter / X"),
                cls="footer-social",
            ),
            Div(cls="footer-sep"),
            P("Built with passion and blood-red code by the SastaSentinels", cls="footer-credit"),
            P("© 2025 SastaSentinels · All Rights Reserved", cls="footer-copy"),
            cls="footer-inner",
        ),
        id="footer",
    )


# ── Route ─────────────────────────────────────────────────────

@rt("/")
def get():
    return (
        Title("SastaSentinels | Elite Esports Squad"),
        crosshair_el(),
        splash_el(),
        Div(id="progress-bar"),
        navbar_el(),
        mobile_menu_el(),
        hero_el(),
        stats_el(),
        quote_el(),
        team_el(),
        matches_el(),
        games_el(),
        highlights_el(),
        join_el(),
        footer_el(),
        Script(src="/static/script.js"),
    )


# Vercel handler
handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, reload_excludes=[".venv"])
