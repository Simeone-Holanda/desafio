<template>
    <div id= "title">
        <h3> {{referencia}}</h3>
        <p> {{ email }}</p>
        <h2 id="tema">{{title_page}}</h2>
    </div>
</template>

<script>

export default {
  name: "Title",
  props: ["referencia","email","title_page"],
}
</script>



<style>

@font-face {
   font-family: Exo;
   src: url(/font/Exo2-VariableFont_wght.ttf);
}

#title {
    font-family: Exo;
    color: cornsilk;
}

#tema {
    color: #ED4D77;
}
</style>



