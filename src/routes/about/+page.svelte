<script lang="ts">
    // import '$lib/styles/global.css';
    import motomachi_hs from '$lib/assets/motomachi_hs.jpg';
    import kogo_js from '$lib/assets/kogo_js.jpg';
    import motomachi_hs_takikun from "$lib/assets/motomachi_hs_takikun.jpeg";
    import motomachi_hs_inside from "$lib/assets/motomachi_hs_inside.jpeg";

    function example(params: { [key: string]: string }) {
        console.log(params);
    }
    import db from '../../db';

    export async function load({ params }) {
        const { slug } = params;
        const { rows } = await db.query('SELECT * FROM posts WHERE slug = $1', [slug]);
        return { props: { post: rows[0] } };
    }
    export let post;
</script>

<div>
    <h1>{post.title}</h1>
    <p>{post.date}</p>
    <article>
        {@html post.content}
    </article>
    <div class="info">
        <p class="info-key">学部生(2022.4~)</p>
        <p class="info-value">大阪大学<wbr>外国語学部</p>
        <p class="info-sub">外国語学科スペイン語専攻 B3</p>
    </div>

    <div class="info">
        <p class="info-key">専攻</p>
        <p class="info-value">言語類型論</p>
    </div>

    <div class="info">
        <p class="info-key">副専攻</p>
        <p class="info-value">コンピュータ科学</p>
        <p class="info-sub">画像は<a href="https://www.visiblethread.com/blog/what-is-nlp-natural-language-processing/"><span>こちらのサイト</span></a>より引用
        <p class="info-sub">(最終閲覧: 2024年6月5日)</p>
    </div>

    <div class="info">
        <p class="info-key">高校生(2019.4~2022.3)</p>
        <p class="info-value">広島市立基町高校</p>
        <a href="http://www.motomachi-h.edu.city.hiroshima.jp/"><img class="responsive-image" src={motomachi_hs} alt="基町高校の外観"></a>
        <p class="info-sub">画像は<a href="https://arch-hiroshima.info/arch/hiroshima/m_highschool.html"><span>こちらのサイト</span></a>より引用
        <p class="info-sub">(最終閲覧: 2024年6月5日)</p>
        <p class="info-sub">綺麗ですよね、これでも公立なんですよ🥰</p>
        <p class="info-sub">映画『<span><a href="https://www.kiminona.com/">君の名は</a></span>』の瀧くんの学校のモデルにもなりました。</p>
        <div style="display: flex; flex-direction: column; gap: 0.5em;">
            <img class="responsive-image" src={motomachi_hs_takikun} alt="作品内での瀧くんの学校">
            <img class="responsive-image" src={motomachi_hs_inside} alt="同じアングルから撮った基町高校の内観">
        </div>
        <p class="info-sub">上が作品内の画像、下が対応する実際の写真です。</p>
        <p class="info-sub">画像は<a href="https://x.com/ichigosama22/status/796670393574518784"><span>こちらのサイト</span></a>より引用
    </div>

    <div class="info">
        <p class="info-key">中学生(2016.4~2019.3)</p>
        <p class="info-value">広島市立庚午中学校</p>
        <a href="https://cms.edu.city.hiroshima.jp/weblog/index.php?id=j1044"><img class="responsive-image" src={kogo_js} alt="庚午中学校の外観"></a>
        <p class="info-sub">サッカー元日本代表の<a href="https://ja.wikipedia.org/wiki/%E6%A7%99%E9%87%8E%E6%99%BA%E7%AB%A0"><span>槙野智章</span></a>の母校でもあります</p>
        <p class="info-sub">画像は<a href="https://www.homemate-research-junior-high-school.com/dtl/00000000000000442704/photo_album/ajax/enlarge/0000037317/10/i"><span>こちらのサイト</span></a>より引用
        <p class="info-sub">(最終閲覧: 2024年6月6日)</p>
    </div>
</div>