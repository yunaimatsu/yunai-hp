<script>
    import { onMount } from 'svelte';
    import '$lib/style/my-bulma-project.css'
    import '$lib/style/global.css'
    onMount(() => {
        const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

        $navbarBurgers.forEach( el => {
            el.addEventListener('click', () => {
                const target = el.dataset.target;
                const $target = document.getElementById(target);
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');
            });
        });
    });
</script>

<nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a href="/" class="navbar-item title">Yu Nai</a>
  
      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
    <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            Home
          </a>
          <a class="navbar-item">
            Documentation
          </a>
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              About
            </a>
            <div class="navbar-dropdown">
              <a class="navbar-item">
                About
              </a>
              <a class="navbar-item">
                Jobs
              </a>
              <a class="navbar-item">
                Contact
              </a>
              <hr class="navbar-divider">
              <a class="navbar-item">
                Report an issue
              </a>
            </div>
          </div>
        </div>
    
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-`primary`">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light">
                Log in
              </a>
            </div>
          </div>
        </div>
    </div>
</nav>

<slot />

<footer class="footer">
    <div class="content has-text-centered">
      <p>© 2024 yunailicensed</p>
    </div>
</footer>

<style>
    .title {
        font-family: "Exo 2", sans-serif;
        font-size: 2em;
        font-weight: 900;
        text-decoration: none;
        text-align: center;
    }
</style>