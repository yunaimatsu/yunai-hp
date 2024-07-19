<script>
  import { onMount, onDestroy } from 'svelte';
  import { fade } from 'svelte/transition';
  export let isLoading = true;

  let messages = [
    "Welcome to Yoshi's homepage",
    "欢迎来到义广的主页",
    "Yoshiのホームページへようこそ",
    "Bienvenido a la página de inicio de Yoshi",
    "Bienvenue sur la page d'accueil de Yoshi",
    "Bem-vindo à página inicial do Yoshi",
    "요시 홈페이지에 오신 것을 환영합니다"
  ];
  let currentMessage = messages[0]; // This will be overridden with a random message on mount.
  let messageIndex = 0;
  let interval;
  let visible = true; // メッセージの表示状態を制御するための変数

  function changeMessage() {
    visible = false; // メッセージを非表示にする
    setTimeout(() => {
      messageIndex = (messageIndex + 1) % messages.length;
      currentMessage = messages[messageIndex];
      visible = true; // 新しいメッセージで再表示
    }, 500); // fadeアウトの時間を考慮して適切な遅延を設定
  }

  onMount(() => {
    // Select a random message as the initial message
    messageIndex = Math.floor(Math.random() * messages.length);
    currentMessage = messages[messageIndex];

    interval = setInterval(changeMessage, 2000); // メッセージの表示時間を調整
  });

  onDestroy(() => {
    clearInterval(interval);
  });
</script>

{#if isLoading}
<div class="loader-container" in:fade={{ duration: 1000 }}>
  {#if visible}
    <p in:fade={{ duration: 500 }} out:fade={{ duration: 500 }}>{currentMessage}</p>
  {/if}
</div>
{/if}

<style>
.loader-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #1E3A8A, #2DD4BF); /* Gradient from marine blue to green */
  font-size: 2rem; /* Increased font size for better readability */
  color: #ffffff; /* Pure white text color */
  transition: background-color 0.5s ease; /* Smooth background color transition */
}

p {
  padding: 0 20px; /* Padding for better readability */
  text-align: center; /* Center align the text */
  font-weight: 600; /* Increased font weight for better readability */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3); /* Subtle text shadow for better legibility */
}
</style>
