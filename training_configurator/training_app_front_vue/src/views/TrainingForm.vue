<template>
    <div class="container">
        <h2> Создать статью </h2>
        <div>
            <div> Название</div>
            <input v-model="training_task.name" class="form-control"/>
        </div>
        <div>
            <div> Тип </div>
            <type-select v-model="training_task.task_type" />
        </div>
        <div>
            <div> Группы мышц </div>
            <musclegroup-type-select v-model="training_task.musclegroup_type" />
        </div>
        <div>
            <div> Длительность</div>
            <input v-model="training_task.duration" class="form-control"/>
        </div>

        <div>
            <div> Описание</div>
            <input v-model="training_task.description" class="form-control"/>
        </div>


        

        <div v-if="training_task.task_type && training_task.task_type.excentions">
            <div v-for=" ext_field in training_task.task_type.excentions" :key="ext_field.name">
                <div> {{ext_field.verbose_name}}</div>
                <input v-model="training_task.addition_info[ext_field.name]" class="form-control"/>
            </div>
        </div>

        <div>
            <div> Тип</div>
            <select v-model="training_task.typ" class="form-control">
                <option  value="AR"> Статья </option>
                <option value="BK"> Книга </option>
            </select>
        </div>

        <button class="btn btn-primary" @click="save"> Сохранить</button>
    </div>
</template>
<script>
import TypeSelect from "@/components/TypeSelect"
import TypeSelect from "@/components/MuscleGroupTypeSelect"
import {TrainingTask} from "@/api"
export default{
    name:'training_task-form',
    data(){
        return {
            training_task:{addition_info:{},}
        }
    },
    components:{
        TypeSelect,
        MusclegroupTypeSelect
    },
    methods:{
        async save(){
            let training_task = {...this.training_task}
            training_task.user = {...this.training_task.user}
            training_task.task_type = training_task.task_type.id  
            await training_task.objects.save(training_task)
            this.$router.push('/training_task/')
        }
    }
}
</script>