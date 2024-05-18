<main>
    <title>yunai official</title>
    <h1 class="philos">Make the world more confortable for all humanity</h1>
    <div>
        <p class="philos">YuNai(Matsuura Yoshihiro)</p>
        <p class="philos">Undergraduate at Osaka University</p>
        <p class="philos">Major: Linguistics</p>
        <p class="philos">Minor: Information Engineering</p>

    </div>
</main>

<style>
    * {
        font-family: 'Roboto', sans-serif;
    }

    main {
        border-color: #333;
        border-radius: 8px;
    }

    .philos {
        color: white;
        text-align: center;
        margin: 1em;
    }

    h1 {
        font-size: 2rem;
        margin-bottom: 1rem;
    }

    /* p {
        color: #666;
        margin-bottom: 2rem;
    } */

    @media only screen and (width <= 300px) {
        h1 {
            font-size: 1em;
        }
    }

    @media only screen and (300px <= width <= 600px) {
        .philos {
            font-size: 1.5em;
        }
    }

    @media only screen and (600px <= width <= 900px) {
        .philos {
            font-size: 2em;
        }
    }

    @media only screen and (900px <= width) {
        .philos {
            font-size: 2.5em;
        }
    }

    @keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}

    }

    .philos {
        animation: fadeIn 3s ease-in-out;
    }
</style>