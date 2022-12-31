<template>
    <div id="nextLink">
    </div>
</template>
<script>
    export default {
        name: "nextLink",
    }
</script>
<style>
    @keyframes goto {
        from {
            margin-right: 100%;
        }

        to {
            margin-right: 0px;
        }
    }

    #textOfGoto {
        position: absolute;
    }

    #nextLink {
        display: flex;
        align-items: center;
        justify-content: center;
        height: calc(100% - 68px - 73.5px);
        background-color: rgb(204, 237, 245);
        animation-name: goto;
        animation-duration: 3s;
    }
</style>