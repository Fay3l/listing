<script setup lang="ts">
const props = defineProps<{
    message: string;
    disabled: boolean;
    type: string;
}>();

</script>

<template>
    <div class="flex justify-center fixed top-0 w-full mt-5" v-if="!props.disabled">
        <div
            :class="[
                'flex items-center flex-col border-2 px-20 rounded-lg',
                props.type === 'Error' ? 'border-red-600 bg-red-100' : 'border-green-600 bg-green-100',
                { shake: !props.disabled }
            ]">
            <p :class="['font-bold', props.type === 'Error' ? 'text-red-600' : 'text-green-600']">{{ props.type }}</p>
            <div>
                <p :class="props.type === 'Error' ? 'text-red-500' : 'text-green-500'">{{ props.message }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
.shake {
    animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
    transform: translate3d(0, 0, 0);
}

@keyframes shake {

    10%,
    90% {
        transform: translate3d(-1px, 0, 0);
    }

    20%,
    80% {
        transform: translate3d(2px, 0, 0);
    }

    30%,
    50%,
    70% {
        transform: translate3d(-4px, 0, 0);
    }

    40%,
    60% {
        transform: translate3d(4px, 0, 0);
    }
}
</style>