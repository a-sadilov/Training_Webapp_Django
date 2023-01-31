<template>
    <div>
        Описание события
        <h2>{{event.name}} {{event.id}}</h2>
        <h2>Дополнительная информация</h2>
        <div v-for="val,key in event.addition_info" :key="key">
            <b>{{key}}</b> {{val}}
            </div>
    </div>
</template>
<script>
import {Event} from "@/api"
export default {
    name:"event-detail",
    data(){
        return {
            event:{}
        }
    },
    methods:{
        async getevent(){
        const id = this.$route.params.id
        this.event = await Event.objects.get(id)
        }
    },
    mounted(){
        this.getevent()
    }
}
</script>