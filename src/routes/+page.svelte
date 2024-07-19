<script>
    import { fly } from 'svelte/transition';
</script>

<div class="introduction">
    <p>当サイトは、わたくし松浦の</p>
    <p>理念</p>
    <p>活動</p>
    <p>プロダクト</p>
    <p>専門知識</p>
    <p>を一ヶ所にまとめたものです</p>
</div>
<div class="history">
    <h2>History</h2>
    <div class="timeline">
        <div class="timeline-item" in:fly={{ x: -200, duration: 500 }}>
            <span class="timeline-year">Year 1</span>
            <p>Started learning programming</p>
        </div>
        <div class="timeline-item" in:fly={{ x: 200, duration: 500, delay: 100 }}>
            <span class="timeline-year">Year 2</span>
            <p>Built my first website</p>
        </div>
        <div class="timeline-item" in:fly={{ x: -200, duration: 500, delay: 200 }}>
            <span class="timeline-year">Year 3</span>
            <p>Joined a software development company</p>
        </div>
        <div class="timeline-item" in:fly={{ x: 200, duration: 500, delay: 300 }}>
            <span class="timeline-year">Year 4</span>
            <p>Developed a mobile app</p>
        </div>
        <div class="timeline-item" in:fly={{ x: -200, duration: 500, delay: 400 }}>
            <span class="timeline-year">Year 5</span>
            <p>Started freelancing</p>
        </div>
    </div>
</div>
<div class="guide">
    <div class="guide__item"><span><a href="https://yunaimatsu.notion.site/Natural-Languages-9718a6a115064bb7bdd30f6aeaa1db4e?pvs=4">自然言語</a></span></div>
    <div class="guide__item"><span><a href="https://yunaimatsu.notion.site/Linguistics-f2130bed7c8d46e9a402b9d8060593e3?pvs=4">言語学</a></span></div>
    <div class="guide__item"><span><a href="https://yunaimatsu.notion.site/Web-Dev-1004a5f02ff948a8be774e816e71a1c9?pvs=4">Web開発</a></span></div>
    <div class="guide__item"><span><a href="https://yunaimatsu.notion.site/Accountings-and-Finance-226a7c3bbf2f4f828b445d2e6ff82085?pvs=4">金融・会計</a></span></div>
    <div class="guide__item"><span><a href="https://yunaimatsu.notion.site/Micro-Macro-Economics-7f0937726b13476f896011a86678ac36?pvs=4">ミクロ経済・マクロ経済</a></span></div>
    <div class="guide__item"><span><a href="https://yunaimatsu.notion.site/Math-90aa66409c4c42e09c0181492004b8a0?pvs=4">数学・統計・物理</a></span></div>
</div>

<style>
    /* Existing styles... */

    .history {
        margin-bottom: 4em;
        padding: 0 1em;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        position: relative;
    }

    .timeline {
        position: relative;
        padding: 20px 0;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .timeline-item {
        background-color: #f9f9f9;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        width: 80%;
        transform: translateX(0);
        transition: transform 0.5s ease;
    }

    .timeline-year {
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        display: inline-block;
        background-color: #006d77;
        color: #fff;
        padding: 5px 10px;
        border-radius: 4px;
    }

    .introduction {
        margin-top: calc(10em + var(--navbar-height));
        margin-bottom: 4em;
        padding: 0 1em;
        text-align: center;
        font-family: 'Roboto', sans-serif;
        color: #333;
    }

    .history {
        margin-bottom: 4em;
        padding: 0 1em;
        text-align: center;
        font-family: 'Roboto', sans-serif;
    }

    .guide {
        display: grid;
        gap: 2em;
        padding: 0 1em;
    }

    @media only screen and (max-width: 768px) {
        .guide__item {
            margin: 2em 0;
            padding: 2em;
            font-size: 1em;
            text-align: center;
            background: linear-gradient(135deg, #006d77, #83c5be);
            border-radius: 8px;
            color: #FFFFFF;
        }
    }

    @media only screen and (min-width: 769px) {
        .guide__item {
            margin: 2em auto;
            padding: 2em;
            font-size: 1.2em;
            text-align: center;
            background: linear-gradient(135deg, #006d77, #83c5be);
            border-radius: 8px;
            color: #FFFFFF;
        }
    }

    a {
        text-decoration: none;
        color: inherit;
        font-weight: bold;
    }

    div {
        animation: fadeIn 2s ease-out forwards;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
