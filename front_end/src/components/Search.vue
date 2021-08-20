<template>
  <div id="Search">
    <div id="divBusca">
      <form action="http://localhost:8080/home">
          <input  v-model="texto" type="text" id="txtBusca" placeholder="Buscar..."/>
          <button @click="$emit('criarTag')" type="submit" id="button"><img src="/img/search.png" id="btnBusca" alt="Buscar"/></button>
      </form>
    </div>

  </div>
</template>

<script>

export default {
  name: "Search",
  emits:['criarTag'],
  data(){
    return {
      texto: ''
    }
  }
}
</script>

<style>

#divBusca{
  background-color:#ffffff;
  height:56px;
  width:382px;
  border:none;
  margin: auto;
}

#txtBusca{
  float:left;
  height: 56px;
  background-color:transparent;
  padding-left:5px;
  font-style:italic;
  font-size:18px;
  border:none;
  padding-left:35%;
}
#button{
  height: 56px;

}

</style>



