<script>
    import '$lib/styles/global.css';
</script>

<div class="introduction">
    <p>当サイトは、わたくし松浦の</p>
    <p>理念</p>
    <p>活動</p>
    <p>プロダクト</p>
    <p>専門知識</p>
    <p>を一ヶ所にまとめたものです</p>
</div>
<div class="guide">
    <div class="guide__item" id="red"><span><a href="https://yunaimatsu.notion.site/Natural-Languages-9718a6a115064bb7bdd30f6aeaa1db4e?pvs=4">自然言語</a></span></div>
    <div class="guide__item" id="orange"><span><a href="https://yunaimatsu.notion.site/Linguistics-f2130bed7c8d46e9a402b9d8060593e3?pvs=4">言語学</a></span></div>
    <div class="guide__item" id="yellow"><span><a href="https://yunaimatsu.notion.site/Web-Dev-1004a5f02ff948a8be774e816e71a1c9?pvs=4">Web開発</a></span></div>
    <div class="guide__item" id="green"><span><a href="https://yunaimatsu.notion.site/Accountings-and-Finance-226a7c3bbf2f4f828b445d2e6ff82085?pvs=4">金融・会計</a></span></div>
    <div class="guide__item" id="blue"><span><a href="https://yunaimatsu.notion.site/Micro-Macro-Economics-7f0937726b13476f896011a86678ac36?pvs=4">ミクロ経済・マクロ経済</a></span></div>
    <div class="guide__item" id="purple"><span><a href="https://yunaimatsu.notion.site/Math-90aa66409c4c42e09c0181492004b8a0?pvs=4">数学・統計・物理</a></span></div>
</div>

<style>
    .introduction {
        margin-top: calc(10em + var(--navbar-height));
        margin-bottom: 10em;
        margin-right: 3em;
        margin-left: 3em;
    }

    .guide {
        display: grid;

    }

    @media only screen and (max-width: 768px) {
        .guide__item {
            margin-top: 3em;
            margin-bottom: 3em;
            margin-right: 3em;
            margin-left: 3em;
            padding-top: 3em;
            padding-bottom: 3em;
        }
        
        .guide__item {
            font-size: 1em; text-align: left; padding-bottom: 1em;
            font-size: 1.2em;
            font-size: 1em; text-align: right; padding-top: 1em;
        }
    }

    @media only screen and (min-width: 769px) {
        .guide__item {
            margin-top: 3em;
            margin-bottom: 3em;
            margin-right: 12em;
            margin-left: 12em;
            padding-top: 3em;
            padding-bottom: 3em;
        }

        .guide__item {
            font-size: 1em;
            text-align: left;
            padding-bottom: 1em;

            font-size: 1.2em;
            font-size: 1em; text-align: right; padding-top: 1em;
        }
    }

    .guide__item {

        text-align: center;

        background-color: #FFFFFF;
    }

    #red {
        background-color: var(--red);
    }

    #orange {
        background-color: var(--orange);
    }

    #yellow {
        background-color: var(--yellow);
    }

    #green {
        background-color: var(--green);
    }

    #blue {
        background-color: var(--blue);
    }

    #purple {
        background-color: var(--purple);
    }
</style>