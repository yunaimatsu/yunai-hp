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
    <div class="guide__item" id="red"><span><a href="">世界の言語</a></span></div>
    <div class="guide__item" id="orange"><span><a href="">言語学</a></span></div>
    <div class="guide__item" id="yellow"><span><a href="https://yunaimatsu.notion.site/Web-Dev-1004a5f02ff948a8be774e816e71a1c9?pvs=4">Web開発</a></span></div>
    <div class="guide__item" id="green"><span><a href="">金融・会計</a></span></div>
    <div class="guide__item" id="blue"><span><a href="">ミクロ経済・マクロ経済</a></span></div>
    <div class="guide__item" id="purple"><span><a href="">統計学</a></span></div>
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
        border-bottom-color: var(--border-color);
        border-bottom-style: solid;
        border-bottom-width: 1px;

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