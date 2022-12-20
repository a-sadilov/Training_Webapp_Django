<template>
    <div>
        Название Упражнения
        <h2>{{TrainingTask.name}} {{TrainingTask.id}}</h2>
        Группы мышц
        <h2>{{TrainingTask.musclegroup_type}}</h2>
        <h2>Дополнительная информация</h2>
        <h2>{{TrainingTask.description}}</h2>
        <h2>Дополнительная информация</h2>
        <h2>{{TrainingTask.description}}</h2>
        <div v-for="val,key in TrainingTask" :key="key">
            <b>{{key}}</b> {{val}}
            </div>
    </div>
</template>
<script>
import {TrainingTask} from "@/api"
export default {
    name:"training-task-detail",
    data(){
        return {
            TrainingTask:{}
        }
    },
    methods:{
        async getTrainingTask(){
        const id = this.$route.params.id
        this.TrainingTask = await TrainingTask.objects.get(id)
        }
    },
    mounted(){
        this.getTrainingTask()
    }
}
</script>