<template>
  <div class="home">
      <Navbar :logo="logo_src" class="navbar"/>
      <span v-if="cards.length == 0">
        <br><br>
        <Message :msg="msg" :v-show="msg"/>
      </span>
      <span v-else>
         <span v-for="(card,indc) in cards" v-bind:key="indc"> 
            <span v-if="indc == 5">
              <div id="divBusca">
                <form action="http://localhost:8080/home" v-on:submit.prevent="find_by_tag">
                    <input  v-model="tag.name" type="text" id="txtBusca" placeholder="Buscar..."/>
                    <button type="submit" id="button"><img src="/img/search.png" id="btnBusca" alt="Buscar"/></button>
                </form>
              </div>
            </span>
            <Card id="card" :texto="card.text" :tag="card.tags[0].name" :indice="indc" />
        </span>
        <span v-if="cards.length < 5"> <div id="divBusca">
                <form action="http://localhost:8080/home" v-on:submit.prevent="find_by_tag">
                    <input  v-model="tag.name" type="text" id="txtBusca" placeholder="Buscar..."/>
                    <button type="submit" id="button"><img src="/img/search.png" id="btnBusca" alt="Buscar"/></button>
                </form>
              </div>
        </span>
      </span>
     

   
  </div>
  
</template>



<script>
import Card from "@/components/Card.vue";
import Navbar from '@/components/Navbar.vue';
import Message from '@/components/Message.vue';
import axios from 'axios'

const url = 'http://127.0.0.1:8000/card/tag'

export default {
  name: "Home",
  components: {
    Card, Navbar, Message
  },
  data(){
    return {
      cards: [],
      logo_src: "/img/brand-insights@3x.svg",
      tag: {
        name: ''
      },
      data_by_tag: '',
      msg: 'Você ainda não tem nenhum card salvo.'
    }
  },
  methods: {
  find_by_tag () {
    console.log("=--=-=-=-=-=-==-=-=-=-=-=-=-=-=")
    axios.post(url, this.tag)
      .then((response) => {
        console.log(this.cards = response.data.data)
      })
      .catch((error) => {
        console.log(error, 'nao funcionou')
      })
  }
},
  mounted(){
    if (this.tag.name == ''){
      fetch('http://127.0.0.1:8000/cards/').then(response => response.json().then(json => this.cards = json.data))
    }else{
      this.cards = this.tag
    }
    
  }
};
</script>

<style>
.home {
  background-color: rgb(247, 247, 247);
  align-items: center;
  overflow: auto;
  height: 800px;
  position: relative;
  
}
.home #card {
  margin: 16px;
}

#divBusca{
  background-color:#cacaca;
  height:69px;
  width:379px;
  margin: auto;
  position: fixed;
  margin-left:21px;
}

#txtBusca{
  float:left;
  height: 53px;
  background-color:transparent;
  font-style:italic;
  font-size:18px;
  border: 2px solid rgb(22, 22, 22);
  padding-left:33%;

}
#button{
  height: 58px;

}

</style>