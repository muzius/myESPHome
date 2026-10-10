import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

bal_lora_ns = cg.esphome_ns.namespace("bal_lora")
BalLora = bal_lora_ns.class_("BalLora", cg.Component)

CONF_BAL_LORA_ID = "bal_lora_id"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(BalLora),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
