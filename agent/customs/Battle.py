import pprint
from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.custom_recognition import CustomRecognition
from maa.context import Context


from .utils import RecoHelper, parse_query_args, Prompt, Judge

# 检测战斗倍速
@AgentServer.custom_recognition("should_set_battle_speed")
class ShouldSetBattleSpeed(CustomRecognition):
    def analyze(
        self, context: Context, argv: CustomRecognition.AnalyzeArg
    ) -> CustomRecognition.AnalyzeResult | bool:
        try:
            # args = parse_query_args(argv)
            reco_helper = RecoHelper(context)
            return reco_helper.recognizeResult("最高倍速_战斗倍速检测")
        except Exception as e:
            return Prompt.error("检测战斗倍速", e)

# 设置战斗倍速
@AgentServer.custom_action("run_set_battle_speed")
class RunSetBattleSpeed(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            # args = parse_query_args(argv)
            context.run_task("最高倍速_战斗倍速开始")
            return True
        except Exception as e:
            return Prompt.error("最高倍速_战斗倍速开始", e)
# 检测自动战斗
@AgentServer.custom_recognition("should_activate_auto_battle")
class ShouldActivateAutoBattle(CustomRecognition):
    def analyze(
        self, context: Context, argv: CustomRecognition.AnalyzeArg
    ) -> CustomRecognition.AnalyzeResult | bool:
        try:
            # args = parse_query_args(argv)
            reco_helper = RecoHelper(context)
            return reco_helper.recognizeResult("激活自动战斗_等待指令")
        except Exception as e:
            return Prompt.error("检测自动战斗", e)
# 执行自动战斗
@AgentServer.custom_action("run_activate_auto_battle")
class RunActivateAutoBattle(CustomAction):
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            # args = parse_query_args(argv)
            context.run_task("激活自动战斗_自动战斗")
            return True
        except Exception as e:
            return Prompt.error("激活自动战斗_自动战斗", e)
# 执行新剧情自动四倍速
@AgentServer.custom_action("run_set_plot_speed")
class RunSetPlotSpeed(CustomAction):
    def run(
      self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult | bool:
        try:
            # args = parse_query_args(argv)
            context.run_task("最高倍速_剧情倍速开始")
            return True
        except Exception as e:
            return Prompt.error("最高倍速_剧情倍速开始", e)