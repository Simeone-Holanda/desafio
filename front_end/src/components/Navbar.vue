<template>
    <div id="nav">
        <div id="links"> 
            <router-link to="/" id=logo-img>
                <img :src="logo">
            </router-link>
                <i class="large material-icons icon-blue"> <img src="/img/perfil.png" id="perfil"> </i>
            <router-link to="/insights" id="logo-url">
                <img src="/img/add.svg" >
            </router-link>
        </div>
        <div id='title'>
            <Title referencia= "Olá, Antonio!" email="antonio.pina@g.globo" title_page="Feed de Insights" title="Feed de Insight" />
        </div>
    </div>
    
</template>

<script>
import Title from './Title.vue'

export default {
    name: 'Navbar',
    props: ['logo'],
    components:{
    Title
  }
}
</script>

<style scoped>

    #nav{
        background-image: url('/img/background.svg');
        width: 414px;
        height: 300px;
        background-repeat: no-repeat;
        display: block;
        
        
    }

    #nav #links{
        display: flex;
    }

    #nav #logo-img{
        margin: auto;
        margin-left: 0;
    }
    #nav #logo-url{
        margin: auto;
        margin-right: 0;
        color: crimson;
    }
    #perfil{
        margin: auto;
        margin-left: -5%;
        margin-top: 30%;
    }
    #title{
        text-align: center;
        font-size: 18pt;
        padding: 0px;
    }
</style>
