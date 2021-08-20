<template>
  
  <div class="about">
    <BanerInsight :logo="logo_src"/>

    <form v-on:submit.prevent="insert" id="form">
      <p id="descricao">INSIGHT</p>
      <textarea name="msg" v-model="card.text" id="msg" rows=32 cols="149" placeholder="Escreva aqui o seu insight" maxlength=400></textarea><br>
        <p id="descricao">CATEGORIA</p>
      <textarea name="tag" v-model="card.tags[0].name" id="tag" rows=32 cols=140 placeholder="Adicione uma categoria (opcional)" maxlength=200></textarea>
      <br> <br>
      <button type="submit" class='button' > PUBLICAR </button>
    </form>
        <Message :msg="msg" v-show="msg"/>
  </div>
</template>

<script>
import BanerInsight from '@/components/BanerInsight.vue';
import Message from '@/components/Message.vue';
import axios from 'axios'

const url = 'http://127.0.0.1:8000/card/'

export default {
  name: "Insight",
  components: {
    BanerInsight, Message
  },
  data(){
    return {
      logo_src: "/img/back.svg",
      card: {
        text: '',
        tags : [{
          name: ''
        },]
      },
      msg: null
    }
  },
  methods: {
    insert () {
      axios.post(url, this.card)
        .then(() => {
          this.msg = "Card criado com sucesso!"
          setTimeout(() => this.msg="", 3000)
        })
        .catch((error) => {
          console.log(error, 'nao funcionou')
        })
    }
  },
}

</script>


<style>

@font-face {
   font-family: Exo;
   src: url(/font/Exo2-VariableFont_wght.ttf);
}

.about {
  align-items: center;
}
#form{
  margin: 20px;
}

#msg {
  width: 350px;
  height: 180px;

}

#descricao{
  color: #000000;
  font-family: Exo;

}
#tag {
  width: 250px;
  height: 66px;
}

.button {
    background-color:#ED4D77;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    width: 382px;
    height: 56px;
    cursor: pointer;
    transition: .5s;
}


</style>
