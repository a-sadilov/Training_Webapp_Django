<template>
    <div>
        Название Упражнения
        <h2>{{Task.name}} {{Task.id}}</h2>
        Группы мышц
        <h2>{{Task.musclegroup_type}}</h2>
        <h2>Дополнительная информация</h2>
        <h2>{{Task.description}}</h2>
        <h2>Дополнительная информация</h2>
        <h2>{{Task.description}}</h2>
        <div v-for="val,key in Task" :key="key">
            <b>{{key}}</b> {{val}}
            </div>
    </div>
</template>
<script>
import {Task} from "@/api"
export default {
    name:"task-detail",
    data(){
        return {
            Task:{}
        }
    },
    methods:{
        async getTask(){
        const id = this.$route.params.id
        this.Task = await Task.objects.get(id)
        }
    },
    mounted(){
        this.getTask()
    }
}
</script>