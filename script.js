/* ============================================================
   SastaSentinels — script.js
   ============================================================ */

// ── Splash Screen ──────────────────────────────────────────

(function () {
    const splash       = document.getElementById('splash');
    const statusEl     = document.getElementById('splashStatus');

    // Lock scroll while splash is up
    document.body.style.overflow = 'hidden';

    function setStatus(text) {
        statusEl.style.opacity = '0';
        setTimeout(() => {
            statusEl.textContent = text;
            statusEl.style.opacity = '1';
        }, 180);
    }

    // Status message timeline
    setTimeout(() => setStatus('LOADING SQUAD...'), 1950);
    setTimeout(() => setStatus('READY  ✓'),         2750);

    // Exit: slide up then remove
    setTimeout(() => {
        splash.classList.add('exit');
        splash.addEventListener('transitionend', () => {
            splash.style.display = 'none';
            document.body.style.overflow = '';
        }, { once: true });
    }, 3200);
})();

// ── Canvas Particle System (mouse-reactive) ────────────────

const canvas = document.getElementById('heroCanvas');
const ctx    = canvas.getContext('2d');

const MOBILE       = () => window.innerWidth < 768;
const PARTICLE_NUM = () => MOBILE() ? 35 : 85;
const CONNECT_DIST = 140;
const COLOR        = 'rgba(204, 0, 0, ';

// Mouse position tracked relative to canvas
const mouse = { x: -9999, y: -9999 };
const MOUSE_RADIUS  = 120;  // attraction radius
const MOUSE_FORCE   = 0.012; // how strongly particles drift toward cursor

let particles = [];

canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
});

canvas.addEventListener('mouseleave', () => {
    mouse.x = -9999;
    mouse.y = -9999;
});

function resizeCanvas() {
    canvas.width  = window.innerWidth;
    canvas.height = Math.round(window.innerHeight * 1.4);
}

class Particle {
    constructor() { this.spawn(); }

    spawn() {
        this.x   = Math.random() * canvas.width;
        this.y   = Math.random() * canvas.height;
        this.vx  = (Math.random() - 0.5) * 0.45;
        this.vy  = (Math.random() - 0.5) * 0.45;
        this.ovx = this.vx; // original velocity
        this.ovy = this.vy;
        this.r   = Math.random() * 1.5 + 0.4;
        this.a   = Math.random() * 0.45 + 0.15;
    }

    update() {
        // Mouse attraction — nudge velocity toward cursor when close enough
        const dx   = mouse.x - this.x;
        const dy   = mouse.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < MOUSE_RADIUS && dist > 0) {
            const strength = (1 - dist / MOUSE_RADIUS) * MOUSE_FORCE;
            this.vx += (dx / dist) * strength * dist;
            this.vy += (dy / dist) * strength * dist;
        }

        // Dampen back toward original drift velocity so particles don't fly off
        this.vx += (this.ovx - this.vx) * 0.04;
        this.vy += (this.ovy - this.vy) * 0.04;

        // Speed cap
        const speed = Math.sqrt(this.vx * this.vx + this.vy * this.vy);
        if (speed > 3) {
            this.vx = (this.vx / speed) * 3;
            this.vy = (this.vy / speed) * 3;
        }

        this.x += this.vx;
        this.y += this.vy;

        // Wrap edges
        if (this.x < 0) this.x = canvas.width;
        if (this.x > canvas.width)  this.x = 0;
        if (this.y < 0) this.y = canvas.height;
        if (this.y > canvas.height) this.y = 0;
    }

    draw() {
        // Particles near the cursor glow slightly brighter
        const dx     = mouse.x - this.x;
        const dy     = mouse.y - this.y;
        const dist   = Math.sqrt(dx * dx + dy * dy);
        const boost  = dist < MOUSE_RADIUS ? (1 - dist / MOUSE_RADIUS) * 0.5 : 0;
        const alpha  = Math.min(this.a + boost, 0.9);

        ctx.beginPath();
        ctx.arc(this.x, this.y, this.r + boost * 1.5, 0, Math.PI * 2);
        ctx.fillStyle = COLOR + alpha + ')';
        ctx.fill();
    }
}

function initParticles() {
    particles = Array.from({ length: PARTICLE_NUM() }, () => new Particle());
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        particles[i].draw();

        for (let j = i + 1; j < particles.length; j++) {
            const dx   = particles[i].x - particles[j].x;
            const dy   = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < CONNECT_DIST) {
                const alpha = (1 - dist / CONNECT_DIST) * 0.18;
                ctx.strokeStyle = COLOR + alpha + ')';
                ctx.lineWidth   = 0.5;
                ctx.beginPath();
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.stroke();
            }
        }
    }

    requestAnimationFrame(animate);
}

resizeCanvas();
initParticles();
animate();

let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        resizeCanvas();
        initParticles();
    }, 150);
});

// ── Scroll Progress + Navbar ───────────────────────────────

const navbar      = document.getElementById('navbar');
const progressBar = document.getElementById('progress-bar');

window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);

    const total    = document.documentElement.scrollHeight - window.innerHeight;
    const progress = total > 0 ? (window.scrollY / total) * 100 : 0;
    progressBar.style.width = progress + '%';
}, { passive: true });

// ── Scroll-spy nav highlight ───────────────────────────────

const navAnchors  = document.querySelectorAll('.nav-links a[href^="#"]');
const sections    = Array.from(navAnchors)
    .map(a => document.querySelector(a.getAttribute('href')))
    .filter(Boolean);

function updateActiveNav() {
    // Pick the section whose top is closest to 30% down the viewport
    const trigger = window.scrollY + window.innerHeight * 0.3;
    let active = sections[0];

    for (const sec of sections) {
        if (sec.offsetTop <= trigger) active = sec;
    }

    navAnchors.forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === '#' + active.id);
    });
}

window.addEventListener('scroll', updateActiveNav, { passive: true });
updateActiveNav(); // set correct state on load

// ── Smooth Scroll ──────────────────────────────────────────

document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        e.preventDefault();
        const target = document.querySelector(a.getAttribute('href'));
        if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
});

// ── Mobile Menu ────────────────────────────────────────────

const hamburger  = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
    const open = mobileMenu.classList.toggle('open');
    hamburger.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
});

document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('open');
        document.body.style.overflow = '';
    });
});

// ── Scroll-reveal (player cards & game cards) ──────────────

const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.player-card, .game-card').forEach(el => {
    revealObserver.observe(el);
});

// ── Game bar fill on reveal ────────────────────────────────

const barObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            const fill = e.target.dataset.fill;
            if (fill) e.target.style.width = fill + '%';
            barObserver.unobserve(e.target);
        }
    });
}, { threshold: 0.4 });

document.querySelectorAll('.game-bar-fill').forEach(bar => {
    barObserver.observe(bar);
});

// ── Staggered game card delays ─────────────────────────────

document.querySelectorAll('.fps-grid .game-card, .story-grid .game-card')
    .forEach((card, i) => {
        card.style.transitionDelay = (i * 0.07) + 's';
    });

// ── Hero typing effect ─────────────────────────────────────

const taglineEl = document.getElementById('tagline');
const text      = 'WE AIM. WE CONQUER. WE DOMINATE.';
let idx = 0;

function typeNext() {
    if (idx <= text.length) {
        taglineEl.innerHTML = text.slice(0, idx) + '<span class="cursor"></span>';
        idx++;
        setTimeout(typeNext, idx === 1 ? 0 : 55);
    } else {
        setTimeout(() => { taglineEl.textContent = text; }, 2500);
    }
}

setTimeout(typeNext, 1600);

// ── Valorant agent background images ──────────────────────

const AGENT_URLS = {
    'BeastM0del':   'https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/fullportrait.png', // Jett
    'WizVoltric':   'https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/fullportrait.png', // Sage
    'GreyWolf':     'https://media.valorant-api.com/agents/22697a3d-45bf-8dd7-4fec-84a9e28c69d7/fullportrait.png', // Chamber
    'KINGPIN':      'https://media.valorant-api.com/agents/f94c3b30-42be-e959-889c-5aa313dba261/fullportrait.png', // Raze
    'Sectumsempra': 'https://media.valorant-api.com/agents/a3bfb853-43b2-7238-a4f1-ad90e9e46bcc/fullportrait.png', // Reyna
    'AgentTrigger': 'https://media.valorant-api.com/agents/0e38b510-41a8-5780-5e8f-568b2a4f2d6c/fullportrait.png', // Iso
    'STING':        'https://media.valorant-api.com/agents/8e253930-4c05-31dd-1b6c-968525494517/fullportrait.png', // Omen
};

document.querySelectorAll('.player-card').forEach(card => {
    const ign = card.querySelector('.player-ign')?.textContent?.trim();
    const url = AGENT_URLS[ign];
    if (!url) return;

    const el = document.createElement('div');
    el.className = 'card-agent';
    el.style.backgroundImage = `url('${url}')`;
    card.querySelector('.card-inner').prepend(el);
});

// ── Custom Crosshair Cursor ────────────────────────────────

const crosshair = document.getElementById('crosshair');
let rafPending = false;
let cursorX = -200, cursorY = -200;

document.addEventListener('mousemove', e => {
    cursorX = e.clientX;
    cursorY = e.clientY;
    if (!rafPending) {
        rafPending = true;
        requestAnimationFrame(() => {
            crosshair.style.transform = `translate(${cursorX}px,${cursorY}px)`;
            rafPending = false;
        });
    }
});

document.addEventListener('mousedown', () => document.body.classList.add('cursor-click'));
document.addEventListener('mouseup',   () => document.body.classList.remove('cursor-click'));

// ── Hero Parallax ──────────────────────────────────────────

window.addEventListener('scroll', () => {
    canvas.style.transform = `translateY(${window.scrollY * 0.35}px)`;
}, { passive: true });

// ── Sound Effects (Web Audio API) ─────────────────────────

const soundToggleBtn  = document.getElementById('soundToggle');
const soundOnIcon     = soundToggleBtn.querySelector('.sound-on');
const soundOffIcon    = soundToggleBtn.querySelector('.sound-off');
let soundEnabled = false;
let audioCtx = null;

function initAudio() {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
}

function playTone(freq, duration, type = 'square', vol = 0.035) {
    if (!soundEnabled || !audioCtx) return;
    const osc  = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(freq * 0.5, audioCtx.currentTime + duration);
    gain.gain.setValueAtTime(vol, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
}

soundToggleBtn.addEventListener('click', () => {
    initAudio();
    soundEnabled = !soundEnabled;
    soundToggleBtn.classList.toggle('active', soundEnabled);
    soundOnIcon.style.display  = soundEnabled ? '' : 'none';
    soundOffIcon.style.display = soundEnabled ? 'none' : '';
    if (soundEnabled) playTone(880, 0.1, 'sine', 0.05);
});

document.querySelectorAll('.player-card, .game-card, .hero-cta, .join-btn').forEach(el => {
    el.addEventListener('mouseenter', () => playTone(600, 0.07, 'square', 0.025));
});

document.querySelectorAll('.hero-cta, .join-btn, .yt-link').forEach(el => {
    el.addEventListener('click', () => playTone(1100, 0.1, 'sine', 0.045));
});

// ── Stats Counter ──────────────────────────────────────────

const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll('.stat-counter-num').forEach(el => {
            const target   = parseInt(el.dataset.target, 10);
            const duration = 1800;
            const step     = 16;
            const inc      = target / (duration / step);
            let current    = 0;
            const timer = setInterval(() => {
                current = Math.min(current + inc, target);
                el.textContent = Math.floor(current).toLocaleString();
                if (current >= target) clearInterval(timer);
            }, step);
        });
        counterObserver.unobserve(entry.target);
    });
}, { threshold: 0.4 });

const statsSection = document.getElementById('stats');
if (statsSection) counterObserver.observe(statsSection);

// ── Highlight video injection ──────────────────────────────

document.querySelectorAll('.highlight-wrap[data-video]').forEach(wrap => {
    const vid = wrap.dataset.video;
    if (!vid || vid.startsWith('VIDEO_ID_')) return;
    const iframe = document.createElement('iframe');
    iframe.className = 'highlight-frame';
    iframe.src = `https://www.youtube.com/embed/${vid}`;
    iframe.title = 'SastaSentinels Highlight';
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    iframe.setAttribute('allowfullscreen', '');
    wrap.innerHTML = '';
    wrap.appendChild(iframe);
});

// ── Extend scroll-reveal to new sections ──────────────────

document.querySelectorAll('.match-row, .highlight-wrap').forEach(el => {
    revealObserver.observe(el);
});

// ── 3D tilt on player cards ────────────────────────────────

document.querySelectorAll('.player-card').forEach(card => {
    const inner = card.querySelector('.card-inner');

    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x    = e.clientX - rect.left;
        const y    = e.clientY - rect.top;
        const cx   = rect.width  / 2;
        const cy   = rect.height / 2;
        const rx   = ((y - cy) / cy) * 7;
        const ry   = ((cx - x) / cx) * 7;

        inner.style.transition = 'background 0.25s, border-color 0.25s';
        inner.style.transform  = `translateY(-5px) rotateX(${rx}deg) rotateY(${ry}deg)`;
    });

    card.addEventListener('mouseleave', () => {
        inner.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        inner.style.transform  = '';
    });
});
