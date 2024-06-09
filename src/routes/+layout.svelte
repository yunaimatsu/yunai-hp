<script>
    import "$lib/style/global.css";
    import { openNavbar, closeNavbar } from './navbar.js';
</script>
<nav class="navBar">
    <a href="/" class="title">YOSHI<wbr>Official</a>
    <button id="sideMenuButton" on:click={openNavbar}>&#9776</button>
    <div class="headMenu">
        <a href="/">Home</a>
        <a href="about">About</a>
    </div>
</nav>

<div class="sideNavBar">
    <a href="/" id="closeButton" on:click={closeNavbar}>&#x274C</a>
    <a href="/">Home</a>
    <a href="about">About</a>
</div>


<slot />

<footer>
    <div class="f-container">
        <p class="lheader">About</p>
        <a href="about" class="f-item">自己紹介・来歴など</a>
    </div>
    <div class="f-container">
        <p class="lheader">連絡</p>
        <a href="mailto:yunaimatsu@gmail.com" class="f-item">Email</a>
        <a href="https://github.com/yunaimatsu" class="f-item">GitHub</a>
        <a href="https://twitter.com/supegoroshiago" class="f-item">Twitter</a>
        <a href="https://www.linkedin.com/in/yoshihiro-matsuura-22179a302/" class="f-item">LinkedIn</a>
        <a href="https://www.facebook.com/people/Matsuura-Yoshihiro/pfbid0rsMP6Z3W1LK4NbTF7Z9to6PBJH3mGoPNXEcS88oc1o31BQjvLeVoaxbfaaEupZk3l/" class="f-item">Facebook</a>
    </div>

    <div class="f-container">
        <p class="lheader">言語</p>
        <a href="language/typology" class="f-item">世界の言語</a>
        <a href="language/linguistics" class="f-item">言語学</a>
        <a href="" class="f-item">自然言語処理(CS)</a>
    </div>

    <div class="f-container">
        <p class="lheader">CS</p>
        <!-- <a href="" class="f-item">CSの全体像</a> -->
        <!-- <a href="" class="f-item">ハードウェア</a> -->
        <!-- <a href="" class="f-item">OS</a> -->
        <a href="cs/software/web-dev" class="f-item">Web開発</a> 
        <!-- <a href="" class="f-item">AI</a>  -->
        <!-- <a href="" class="f-item">Python</a> -->
        <!-- <a href="" class="f-item">Notion</a> -->
        <!-- <a href="" class="f-item">Google Office</a>
        <a href="" class="f-item">Microsoft Office</a>
        <a href="" class="f-item">ネットワーク</a> -->
    </div>
    
    <div class="f-container">
        <p class="lheader">経済 (β)</p>
        <!-- <a href="" class="f-item">経済学の全体像</a> -->
        <!-- <a href="" class="f-item">金融</a> -->
        <!-- <a href="" class="f-item">会計</a> -->
        <!-- <a href="" class="f-item">ミクロ経済</a>  -->
        <!-- <a href="" class="f-item">マクロ経済</a> -->
    </div>

    <div class="f-container">
        <p class="lheader">数理 (β)</p>
        <a href="" class="f-item">統計</a>
        <a href="" class="f-item">解析</a>
        <a href="" class="f-item">集合・論理</a>
    </div>

    <div class="f-container">
        <p class="lheader">音楽［開発中］</p>
        <a href="" class="f-item">世界の楽器</a>
        <a href="" class="f-item">DTM(CS)</a>
        <a href="" class="f-item">音楽史</a>
        <a href="" class="f-item">音楽理論</a>
    </div>

    <div class="f-container">
        <p class="lheader">機械工学［開発中］</p>
        <a href="" class="f-item">機械工学の全体像</a>
        <a href="" class="f-item">流体力学</a>
        <a href="" class="f-item">材料力学</a>
        <a href="" class="f-item">熱力学</a>
        <a href="" class="f-item">機械力学</a>
    </div>

    <div class="liscence">
        <p class="liscence-text">© 2024 yunai</p>
    </div>
</footer>