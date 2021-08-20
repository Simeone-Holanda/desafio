<template>
  <div id="card">
    <p>{{texto}}</p>  
    <span id="tag">{{tag}}</span>
    <br>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: ["texto","tag","indice"]
}
</script>

<style>
  @font-face {
    font-family: Exo;
    src: url(/font/Exo2-VariableFont_wght.ttf);
  }

  #card {
    background-color: #c7c7c7;
    width: 382px;
    height: 67px;
    border-radius: 8px;
    color: #000000;
    text-align: center;
    font-size: 14px;
    font-weight: 500;
    line-height: 16px;
    box-sizing: border-box;
    overflow: auto;
    margin: 20px;
    font-family: Exo;
  }

  #card #tag {
    color: #ED4D77;
    font-weight: 700;
    font-size: 10px;
    width: 61px;
    height: 12px;
    text-align: center;
    font-family: Exo;
  }

</style>



